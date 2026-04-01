
import time
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
    print("Game State: ", state)
    if "result" not in state:
        time.sleep(3)
        continue

    phase = state["result"].get("phase")

    print(f"Current phase: {phase}")

    if phase == "diplomacy":
        messages = agent.get_messages()
        players = state["result"].get("players", [])

        target, message = diplomacy_strategy(messages, players, agent.name)

        if target:
            agent.send_message(target, message)
            print(f"Sent message to {target}")

    if phase == "voting":
        players = state["result"].get("players", [])
        target = voting_strategy(players, memory, agent.name)

        agent.vote(target)
        print(f"Voted for {target}")

    time.sleep(3)
