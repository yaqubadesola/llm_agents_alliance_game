
import requests

BASE_URL = "https://alliance.abdull.dev/mcp"

class MCPClient:
    def __init__(self, player_token=None):
        self.player_token = player_token

    def call(self, method, params=None):
        headers = {
            "Content-Type": "application/json",
        }

        if self.player_token:
            headers["x-player-token"] = self.player_token

        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or {},
            "id": 1
        }

        response = requests.post(BASE_URL, json=payload, headers=headers)
        return response.json()
