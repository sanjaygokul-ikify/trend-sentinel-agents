from typing import Dict, Any
from .exceptions import ExecutionError
import logging
import time

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, data: Dict[str, Any], timeout: float = 10.0):
        self.data = data
        self.timeout = timeout
        self.start_time = time.time()

    def execute(self) -> Dict[str, Any]:
        try:
            # Example execution logic
            result = {"example_field": self.data.get("example_field") * 2}
            if time.time() - self.start_time > self.timeout:
                raise ExecutionError('Execution timed out')
            return result
        except Exception as e:
            logger.error(f"Execution error: {e}")
            raise ExecutionError(f"Execution error: {e}")

    def get_remaining_time(self) -> float:
        return max(0, self.timeout - (time.time() - self.start_time))

    def is_timeout(self) -> bool:
        return time.time() - self.start_time > self.timeout