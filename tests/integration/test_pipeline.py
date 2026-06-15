from packages.core import PolicyEngine, Policy, Anomaly
from packages.services import Orchestrator
from packages.utils import logging
import unittest

example_policy_data = {"example_field": 15}

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        policy_engine = PolicyEngine([])
        orchestrator = Orchestrator(policy_engine)
        policy_engine.add_policy(Policy("Example Policy", lambda data: [Anomaly("Example Anomaly", "Example anomaly description")]))
        anomalies = orchestrator.run(example_policy_data)
        self.assertEqual(len(anomalies), 1)
        self.assertEqual(anomalies[0].name, "Example Anomaly")

if __name__ == '__main__':
    unittest.main()