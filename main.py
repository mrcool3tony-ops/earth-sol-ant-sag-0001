from src.core.event_bus import EventBus
from src.core.state_machine import StateMachine
from src.systems.dialogue_system import DialogueSystem
from src.systems.inventory_system import InventorySystem
from src.systems.save_manager import SaveManager

bus = EventBus()
fsm = StateMachine("BOOT")
fsm.add_transition("BOOT", "START_GAME", "PLAYING")
fsm.add_transition("PLAYING", "END_DEMO", "COMPLETED")

registry = {"core_shard": {"name": "Antipolo Core Shard"}}
inv = InventorySystem(registry)
saver = SaveManager()
flags = {"humanity_index": 50}

story = {
    "start": {
        "speaker": "NEXUS AI",
        "text": "Welcome to Antipolo Core Nexus. Verify your intent, Pinocchio.",
        "choices": [
            {"label": "Sync with the Core (Gain Shard)", "next": "synced", "effects": {"synced": True}},
            {"label": "Bypass Firewall (Keep Autonomy)", "next": "bypassed", "effects": {"humanity_index": 80}}
        ]
    },
    "synced": {"speaker": "NEXUS AI", "text": "Core Shard acquired. Protocol aligned.", "choices": []},
    "bypassed": {"speaker": "SYSTEM", "text": "Firewall bypassed. Autonomy preserved.", "choices": []}
}

bus.subscribe("ITEM_GRANTED", lambda item_id: inv.add_item(item_id))

def run():
    print(f"[STATE] {fsm.trigger('START_GAME')}")
    dlg = DialogueSystem(story)
    node = dlg.start("start")
    while node:
        print(f"\n{node['speaker']}: {node['text']}")
        if not node["choices"]:
            break
        for i, c in enumerate(node["choices"]):
            print(f"  [{i}] {c['label']}")
        pick = int(input("Select choice: "))
        node = dlg.choose(pick, flags)
        if flags.get("synced"):
            bus.emit("ITEM_GRANTED", item_id="core_shard")

    saver.save("slot1", {"state": fsm.trigger("END_DEMO"), "flags": flags, "inventory": inv.items})
    print("\n[SAVED] slot1.json ->", saver.load("slot1"))

if __name__ == "__main__":
    run()
