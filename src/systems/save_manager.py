import json
from pathlib import Path

class SaveManager:
    def __init__(self, save_dir="src/saves"):
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)

    def save(self, slot_name, payload):
        path = self.save_dir / f"{slot_name}.json"
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def load(self, slot_name):
        path = self.save_dir / f"{slot_name}.json"
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
