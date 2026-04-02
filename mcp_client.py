import requests
import json

BASE_URL = "https://alliance.abdull.dev/mcp"

class MCPClient:
    def __init__(self, player_token=None):
        self.player_token = player_token

    def call(self, tool_name, params=None):

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream"
        }

        if self.player_token:
            headers["x-player-token"] = self.player_token

        payload = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": params or {}
            },
            "id": 1
        }

        response = requests.post(
            BASE_URL,
            headers=headers,
            json=payload,
            stream=True
        )

        for line in response.iter_lines():

            if line:
                decoded = line.decode("utf-8")

                if decoded.startswith("data:"):
                    data = decoded.replace("data:", "").strip()

                    try:
                        return json.loads(data)
                    except:
                        continue

        return {}