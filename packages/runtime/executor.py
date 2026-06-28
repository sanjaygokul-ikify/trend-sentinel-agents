from typing import Dict, Any
from .exceptions import ExecutionError
import logging
import time

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, data: Dict[str, Any], timeout: float = 10.0):
        self.data = data
        self.timeout = timeout

    def execute(self) -> Dict[str, Any]:
        try:
            # Example execution logic
            start_time = time.time()
            result = {"example_field": self.data.get("example_field") * 2}
            if time.time() - start_time > self.timeout:
                raise ExecutionError('Execution timed out')
            return result
        except Exception as e:
            logger.error(f"Execution error: {e}")
            raise ExecutionError(f"Execution error: {e}")

class ExecutionError(Exception):
    pass