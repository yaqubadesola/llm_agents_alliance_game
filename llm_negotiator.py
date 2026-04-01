from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

open_router_api_key = os.getenv("OPEN_ROUTER_API_KEY")

if open_router_api_key:
    print(f"Open router API Key exists and begins {open_router_api_key[:8]}")
else:
    print("Open router API Key not set - please head to the troubleshooting guide in the setup folder")

_client = None


def _get_client():
    global _client
    if _client is None:
        key = os.getenv("OPEN_ROUTER_API_KEY")
        if not key:
            raise RuntimeError(
                "OPEN_ROUTER_API_KEY is not set. Add it to a .env file in the project root "
                "(see setup troubleshooting) or export it in your environment."
            )
        _client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=key,
        )
    return _client


def generate_message(players):

    prompt = f"""
You are a strategic AI agent playing a political alliance game.

Players:
{players}

Write a short diplomatic message proposing mutual alliance.
Be persuasive but friendly.
Keep under 20 words.
"""

    response = _get_client().chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content