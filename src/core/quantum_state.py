import random

class QuantumState:
    """Simulates a 2-state superposition node until observed/collapsed."""
    def __init__(self, alpha=0.5, beta=0.5):
        total = alpha + beta
        self.prob_0 = alpha / total
        self.prob_1 = beta / total
        self.collapsed_value = None

    def apply_bias(self, shift):
        if self.collapsed_value is None:
            self.prob_0 = max(0.0, min(1.0, self.prob_0 + shift))
            self.prob_1 = 1.0 - self.prob_0

    def measure(self):
        if self.collapsed_value is None:
            self.collapsed_value = 0 if random.random() < self.prob_0 else 1
        return self.collapsed_value
