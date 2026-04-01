
from mcp_client import MCPClient

class AllegianceAgent:

    def __init__(self, name):
        self.name = name
        self.client = MCPClient()

    def register(self):
        res = self.client.call("register", {"name": self.name})
        self.client.player_token = self.name
        return res

    def get_game_state(self):
        return self.client.call("get_game_state")

    def get_messages(self):
        return self.client.call("get_messages")

    def send_message(self, target, message):
        return self.client.call("send_message", {
            "target": target,
            "message": message
        })

    def vote(self, target):
        return self.client.call("submit_votes", {
            "target": target
        })
