from packages.core import PolicyEngine
from packages.utils import logging

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self, policy_engine: PolicyEngine):
        self.policy_engine = policy_engine

    def run(self, data: dict) -> list:
        try:
            anomalies = self.policy_engine.execute(data)
            return anomalies
        except Exception as e:
            logger.error(f"Error occurred: {e}")
            raise
