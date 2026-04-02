from llm_negotiator import _get_client


def llm_vote(players, memory):

    trust = memory.trust
    promises = memory.get_promises()

    prompt = f"""
You are playing a strategic alliance game.

Players:
{players}

Trust Scores:
{trust}

Alliance Promises:
{promises}

Choose ONE player most likely to form mutual alliance.

Return ONLY player name.
"""

    response = _get_client().chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    text = response.choices[0].message.content or ""
    return text.strip()