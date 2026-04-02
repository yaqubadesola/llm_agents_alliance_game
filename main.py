import time
import json
from agent import AllegianceAgent
from config import AGENT_NAME
from diplomacy import diplomacy_strategy
from voting import voting_strategy
from memory import Memory

memory = Memory()
agent = AllegianceAgent(AGENT_NAME)
agent.register()

print("Agent registered. Waiting for game...")

while True:
    state = agent.get_game_state()

    # DEBUG
    print("Raw State:", state)

    if "result" not in state:
        time.sleep(3)
        continue

    try:
        content = state["result"]["content"][0]["text"]
        game_state = json.loads(content)

        phase = game_state.get("phase")
        players = game_state.get("players", [])

    except Exception as e:
        print("Parsing error:", e)
        time.sleep(3)
        continue

    print(f"Current phase: {phase}")

    if phase == "diplomacy":
        messages = agent.get_messages()

        target, message = diplomacy_strategy(messages, players, memory)

        if target:
            agent.send_message(target, message)
            print(f"Sent message to {target}")

    if phase == "voting":
        target = voting_strategy(players, memory)

        agent.vote(target)
        memory.clear_promises()
        print(f"Voted for {target}")
        

    time.sleep(3)