import asyncio
import click
import json
import re
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions


async def analyze_image_for_stocks(image_path: str) -> dict:
    """Vision analysis to extract company names and identify stock symbols from image."""
    abs_path = str(Path(image_path).resolve())

    prompt = f"""Read and analyze the image at: {abs_path}

Extract ALL company names that might be publicly traded on Indian stock exchanges (NSE or BSE).

Look for:
- Company names in logos, headers, or text
- App names that belong to publicly traded companies
- Brand names of listed companies

For EACH company found, identify the NSE/BSE stock symbol based on your knowledge.

Return ONLY a JSON object with this structure, nothing else:
{{
    "stocks": [
        {{
            "company": "Company Name",
            "symbol": "SYMBOL",
            "exchange": "NSE" or "BSE"
        }}
    ],
    "reasoning": "Brief explanation of companies identified"
}}

If no publicly traded companies found, return:
{{
    "stocks": [],
    "reasoning": "No publicly traded companies identified"
}}"""

    import sys
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

    # Parse JSON from response - find balanced braces
    def extract_json_object(text: str) -> str | None:
        start = text.find('{')
        if start == -1:
            return None
        depth = 0
        for i, char in enumerate(text[start:], start):
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
                if depth == 0:
                    return text[start:i+1]
        return None

    json_str = extract_json_object(result_text)
    if json_str:
        return json.loads(json_str)

    return {
        "stocks": [],
        "reasoning": "Failed to parse response"
    }


async def find_stocks(image_path: str) -> list[dict]:
    """Main logic - image analysis only, no web searches."""
    result = await analyze_image_for_stocks(image_path)
    return result.get("stocks", [])


@click.command()
@click.argument("image_path", type=click.Path(exists=True))
@click.option("--verbose", "-v", is_flag=True, help="Show full analysis result with reasoning")
def main(image_path: str, verbose: bool):
    """Find all NSE/BSE stock symbols from a screenshot (lite version - no web search)."""
    if verbose:
        result = asyncio.run(analyze_image_for_stocks(image_path))
        print(json.dumps(result, indent=2))
    else:
        stocks = asyncio.run(find_stocks(image_path))
        print(json.dumps({"stocks": stocks}))


if __name__ == "__main__":
    main()
