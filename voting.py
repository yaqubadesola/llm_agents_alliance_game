import random
from config import AGENT_NAME
from llm_voting import llm_vote


def voting_strategy(players, memory):

    players = [p for p in players if p != AGENT_NAME]

    if not players:
        return ""

    # 1. mutual alliance priority
    promises = memory.get_promises()

    for p in promises:
        if p in players:
            print(f"Voting for promised ally: {p}")
            return p

    # 2. trusted player
    trusted = memory.get_best_trusted()

    if trusted and trusted in players:
        print(f"Voting for trusted player: {trusted}")
        return trusted

    # 3. LLM voting
    try:
        llm_choice = llm_vote(players, memory)

        if llm_choice in players:
            print(f"LLM vote: {llm_choice}")
            return llm_choice

    except Exception as e:
        print("LLM voting failed:", e)

    # 4. fallback random
    target = random.choice(players)
    print(f"Random vote: {target}")
    return target