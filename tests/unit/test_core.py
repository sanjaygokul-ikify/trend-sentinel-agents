from packages.core import PolicyEngine, Policy, Anomaly
import unittest

example_policy_data = {"example_field": 15}

class TestPolicyEngine(unittest.TestCase):
    def test_policy_engine(self):
        policy_engine = PolicyEngine([])
        self.assertEqual(policy_engine.execute({}), [])

    def test_policy_execute(self):
        policy = Policy("Example Policy", lambda data: [Anomaly("Example Anomaly", "Example anomaly description")])
        policy_engine = PolicyEngine([policy])
        anomalies = policy_engine.execute(example_policy_data)
        self.assertEqual(len(anomalies), 1)
        self.assertEqual(anomalies[0].name, "Example Anomaly")

if __name__ == '__main__':
    unittest.main() 
