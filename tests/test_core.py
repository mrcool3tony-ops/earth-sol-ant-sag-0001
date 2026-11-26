import unittest
from src.core.state_machine import StateMachine
from src.core.quantum_state import QuantumState
from src.systems.inventory_system import InventorySystem

class TestCoreArchitecture(unittest.TestCase):
    def test_state_transition(self):
        fsm = StateMachine("BOOT")
        fsm.add_transition("BOOT", "START", "PLAYING")
        self.assertEqual(fsm.trigger("START"), "PLAYING")

    def test_quantum_collapse(self):
        q = QuantumState(0.5, 0.5)
        result = q.measure()
        self.assertIn(result, (0, 1))
        self.assertEqual(q.measure(), result)

    def test_inventory_add_remove(self):
        inv = InventorySystem({"shard": {"name": "Core Shard"}})
        inv.add_item("shard", 2)
        self.assertTrue(inv.remove_item("shard", 1))
        self.assertEqual(inv.items["shard"], 1)

if __name__ == "__main__":
    unittest.main()
