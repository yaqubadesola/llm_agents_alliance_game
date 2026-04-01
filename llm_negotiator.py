from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

_client = None


def _get_client():
    global _client
    if _client is None:
        key = os.getenv("OPEN_ROUTER_API_KEY")
        if not key:
            raise RuntimeError(
                "OPEN_ROUTER_API_KEY is not set. Add it to a .env file in the project root "
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