import asyncio
import click
import json
import re
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions

MAX_SEARCHES_PER_COMPANY = 3
MAX_ATTEMPTS = 2


async def extract_companies(image_path: str) -> list[str]:
    """Vision analysis to extract company names from image."""
    abs_path = str(Path(image_path).resolve())

    prompt = f"""Read and analyze the image at: {abs_path}

Extract any company names that might be publicly traded on Indian stock exchanges (NSE or BSE).

Look for:
- Company names in logos, headers, or text
- App names that belong to publicly traded companies
- Brand names of listed companies

Return ONLY a JSON array of company names found, nothing else. If no companies found, return [].
Example: ["Reliance Industries", "Infosys"]"""

    result_text = ""
    async for event in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            max_turns=2,
            allowed_tools=["Read"],
        ),
    ):
        event_type = type(event).__name__
        if event_type == "AssistantMessage" and hasattr(event, "content"):
            for block in event.content:
                if hasattr(block, "text"):
                    result_text += block.text
        elif event_type == "ResultMessage" and hasattr(event, "result"):
            if event.result:
                result_text += str(event.result)

    # Parse JSON from response
    match = re.search(r'\[.*?\]', result_text, re.DOTALL)
    if match:
        return json.loads(match.group())
    return []


async def search_for_symbol(search_query: str) -> dict | None:
    """Single web search, returns {"symbol": X, "exchange": Y} or None."""
    prompt = f"""Search for: {search_query}

Find the official NSE or BSE stock symbol/ticker for this company.

Return ONLY a JSON object with the symbol and exchange, nothing else:
- If found: {{"symbol": "SYMBOL", "exchange": "NSE"}} or {{"symbol": "SYMBOL", "exchange": "BSE"}}
- Prefer NSE over BSE if both are available
- If not found or not a listed company: {{"symbol": null, "exchange": null}}

Return only the JSON, no explanation."""

    result_text = ""
    async for event in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            max_turns=2,
            allowed_tools=["WebSearch"],
        ),
    ):
        event_type = type(event).__name__
        if event_type == "AssistantMessage" and hasattr(event, "content"):
            for block in event.content:
                if hasattr(block, "text"):
                    result_text += block.text
        elif event_type == "ResultMessage" and hasattr(event, "result"):
            if event.result:
                result_text += str(event.result)

    # Parse JSON from response
    match = re.search(r'\{.*?\}', result_text, re.DOTALL)
    if match:
        data = json.loads(match.group())
        if data.get("symbol"):
            return data
    return None


async def generate_alternates(company_name: str) -> list[str]:
    """LLM suggests alternate names/abbreviations for retry."""
    prompt = f"""Given this company name: "{company_name}"

Generate alternate names, abbreviations, or parent company names that might help find its Indian stock listing.

For example:
- "Zerodha" -> ["Zerodha", "Zerodha Broking"] (but Zerodha is not listed)
- "ICICI Bank app" -> ["ICICI Bank", "ICICI"]
- "Groww" -> ["Groww", "Nextbillion Technology"] (parent company)

Return ONLY a JSON array of alternate names to search, nothing else.
Include the original name plus variations."""

    result_text = ""
    async for event in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            max_turns=1,
            allowed_tools=[],
        ),
    ):
        event_type = type(event).__name__
        if event_type == "AssistantMessage" and hasattr(event, "content"):
            for block in event.content:
                if hasattr(block, "text"):
                    result_text += block.text
        elif event_type == "ResultMessage" and hasattr(event, "result"):
            if event.result:
                result_text += str(event.result)

    match = re.search(r'\[.*?\]', result_text, re.DOTALL)
    if match:
        return json.loads(match.group())
    return [company_name]


async def find_symbol_for_company(company: str) -> dict | None:
    """Find symbol for a single company with retries."""
    queries = [
        f"{company} NSE stock symbol",
        f"{company} BSE stock symbol",
        f"{company} India stock ticker",
    ]

    # First attempt with original name
    for q in queries[:MAX_SEARCHES_PER_COMPANY]:
        result = await search_for_symbol(q)
        if result:
            return {"company": company, "symbol": result["symbol"], "exchange": result["exchange"]}

    # Second attempt with alternate names
    alternates = await generate_alternates(company)
    for alt in alternates:
        if alt == company:
            continue
        result = await search_for_symbol(f"{alt} NSE BSE stock symbol")
        if result:
            return {"company": company, "symbol": result["symbol"], "exchange": result["exchange"]}

    return None


async def find_all_symbols(image_path: str) -> list[dict]:
    """Find symbols for all companies in the image."""
    companies = await extract_companies(image_path)

    if not companies:
        return []

    # Search for each company concurrently
    tasks = [find_symbol_for_company(company) for company in companies]
    results = await asyncio.gather(*tasks)

    # Filter out None results and return found symbols
    return [r for r in results if r is not None]


@click.command()
@click.argument("image_path", type=click.Path(exists=True))
def main(image_path: str):
    """Find NSE/BSE stock symbols for all companies in a screenshot."""
    symbols = asyncio.run(find_all_symbols(image_path))
    print(json.dumps({"symbols": symbols}))


if __name__ == "__main__":
    main()
