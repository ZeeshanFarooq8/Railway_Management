import logging
import sys

# Create logger
logger = logging.getLogger("railway_app")
logger.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

# Stream handler (console)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

# Add handler only once
if not logger.handlers:
    logger.addHandler(stream_handler)
