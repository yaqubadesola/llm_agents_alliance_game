import random


def voting_strategy(players, memory, self_name):

    if not players:
        return ""

    others = [p for p in players if p != self_name]

    if not others:
        return ""

    best = memory.get_best_player()
    if best and best in others:
        return best

    return random.choice(others)