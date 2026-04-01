import random
from llm_negotiator import generate_message

def diplomacy_strategy(messages, players, self_name):

    if not players:
        return None, None

    players = [p for p in players if p != self_name]

    if not players:
        return None, None

    target = random.choice(players)

    message = generate_message(players)

    return target, message