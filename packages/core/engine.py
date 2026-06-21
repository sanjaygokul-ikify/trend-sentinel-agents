from typing import List, Dict, Any
from .types import Policy, Anomaly
from .exceptions import PolicyError, AnomalyError
import logging

logger = logging.getLogger(__name__)

class PolicyEngine:
    def __init__(self, policies: List[Policy]):
        self.policies = policies
        self.anomalies = []

    def execute(self, data: Dict[str, Any]) -> List[Anomaly]:
        anomalies = []
        for policy in self.policies:
            try:
                policy_anomalies = policy.execute(data)
                if policy_anomalies:
                    anomalies.extend(policy_anomalies)
            except PolicyError as e:
                logger.error(f"Policy error: {e}")
        return anomalies

    def get_anomalies(self) -> List[Anomaly]:
        return self.anomalies

    def clear_anomalies(self):
        self.anomalies = []

    def add_policy(self, policy: Policy):
        self.policies.append(policy)

    def remove_policy(self, policy: Policy):
        self.policies.remove(policy)

class Policy:
    def __init__(self, name: str, func: callable):
        self.name: str = name
        self.func: callable = func

    def execute(self, data: Dict[str, Any]) -> List[Anomaly]:
        return self.func(data)

class Anomaly:
    def __init__(self, name: str, description: str):
        self.name: str = name
        self.description: str = description

def example_policy(data: Dict[str, Any]) -> List[Anomaly]:
    # Example policy function
    anomalies = []
    if data.get("example_field") > 10:
        anomalies.append(Anomaly("Example Anomaly", "Example anomaly description"))
    return anomalies

# Create a policy engine
engine = PolicyEngine([Policy("Example Policy", example_policy)])

# Example usage
data = {"example_field": 15}
anomalies = engine.execute(data)
for anomaly in anomalies:
    logger.warning(f"Anomaly detected: {anomaly.name} - {anomaly.description}")