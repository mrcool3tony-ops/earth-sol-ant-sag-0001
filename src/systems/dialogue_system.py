class DialogueSystem:
    def __init__(self, nodes):
        self.nodes = nodes
        self.current_id = None

    def start(self, node_id="start"):
        self.current_id = node_id
        return self.nodes.get(self.current_id)

    def choose(self, choice_index, flags):
        node = self.nodes.get(self.current_id, {})
        choices = node.get("choices", [])
        if 0 <= choice_index < len(choices):
            choice = choices[choice_index]
            flags.update(choice.get("effects", {}))
            self.current_id = choice.get("next")
        return self.nodes.get(self.current_id)
