from typing import Optional


class Memory:
    def __init__(self) -> None:
        self.trust: dict[str, int] = {}
        self.promises: set[str] = set()

    def add_promise(self, player: str) -> None:
        self.promises.add(player)

    def clear_promises(self) -> None:
        self.promises = set()

    def get_promises(self) -> list[str]:
        return list(self.promises)

    def increase_trust(self, player: str) -> None:
        self.trust[player] = self.trust.get(player, 0) + 1

    def decrease_trust(self, player: str) -> None:
        self.trust[player] = self.trust.get(player, 0) - 1

    def get_best_trusted(self) -> Optional[str]:
        if not self.trust:
            return None
        return max(self.trust, key=lambda name: self.trust[name])
