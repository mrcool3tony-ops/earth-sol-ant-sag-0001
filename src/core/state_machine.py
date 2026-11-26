class StateMachine:
    def __init__(self, initial_state="BOOT"):
        self.state = initial_state
        self.transitions = {}

    def add_transition(self, from_state, event, to_state):
        self.transitions[(from_state, event)] = to_state

    def trigger(self, event):
        next_state = self.transitions.get((self.state, event))
        if next_state:
            self.state = next_state
        return self.state
