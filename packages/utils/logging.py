import logging

logger = logging.getLogger(__name__)

def configure_logging(level=logging.INFO):
    logging.basicConfig(level=level)
