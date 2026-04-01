from typing import Optional


class Memory:

    def __init__(self) -> None:
        self.trust: dict[str, int] = {}

    def increase_trust(self, player):

        if player not in self.trust:
            self.trust[player] = 0

        self.trust[player] += 1

    def decrease_trust(self, player):

        if player not in self.trust:
            self.trust[player] = 0

        self.trust[player] -= 1

    def get_best_player(self) -> Optional[str]:

        if not self.trust:
            return None

        return max(self.trust, key=lambda name: self.trust[name])