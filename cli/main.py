import argparse
from packages.core import PolicyEngine
from packages.utils import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Policy Engine CLI')
parser.add_argument('--policy', help='Policy name')
parser.add_argument('--data', help='Data to execute policy on')

args = parser.parse_args()

policy_engine = PolicyEngine([])

if args.policy and args.data:
    data = {'example_field': 15}
    try:
        anomalies = policy_engine.execute(data)
        for anomaly in anomalies:
            logger.warning(f"Anomaly detected: {anomaly.name} - {anomaly.description}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
