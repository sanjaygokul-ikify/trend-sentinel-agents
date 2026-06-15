import logging
from typing import Tuple

logger = logging.getLogger(__name__)

def calculate_metrics(data: Tuple[float, float]) -> Tuple[float, float]:
    try:
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return mean, variance
    except ZeroDivisionError as e:
        logger.error("Cannot calculate metrics for empty data", exc_info=e)
        raise ValueError("Cannot calculate metrics for empty data") from e