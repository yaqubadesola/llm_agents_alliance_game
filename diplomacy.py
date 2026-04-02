import json
import random
from config import AGENT_NAME
from llm_negotiator import generate_message


def diplomacy_strategy(messages, players, memory):

    # Try detect incoming alliance offers
    try:
        content = messages["result"]["content"][0]["text"]
        parsed = json.loads(content)
        msgs = parsed.get("messages", [])

        for msg in msgs:
            sender = msg.get("from")
            text = msg.get("message", "").lower()

            if sender and sender != AGENT_NAME:
                if "alliance" in text or "mutual" in text:
                    memory.add_promise(sender)

                    # Use LLM to respond
                    response = generate_message([sender])

                    return sender, response

    except Exception as e:
        print("Message parsing error:", e)

    # No incoming alliance → propose new one
    players = [p for p in players if p != AGENT_NAME]

    if not players:
        return None, None

    target = random.choice(players)

    # Use LLM here
    message = generate_message(players)

    return target, message