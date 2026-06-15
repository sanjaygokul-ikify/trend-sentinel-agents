import unittest
from packages.utils import logging

class TestRuntime(unittest.TestCase):
    def test_logging_configure(self):
        logging.configure_logging(level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logger.debug("Test debug message")

if __name__ == '__main__':
    unittest.main()