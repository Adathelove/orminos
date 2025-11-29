import logging
from .colors import (
    RESET, TEAL, ORANGE, PINK, RED, DARK_RED, YELLOW, GREEN
)

# Configure base logging system once.
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)

logger = logging.getLogger("orminos")

def _emit(tag, color, msg):
    logger.info(f"{color}[{tag}]{RESET} {msg}")

def info(msg):       _emit("INFO", TEAL, msg)
def debug(msg):      _emit("DEBUG", PINK, msg)
def warn(msg):       _emit("WARN", YELLOW, msg)
def fail(msg):       _emit("FAIL", RED, msg)
def abort(msg):      _emit("ABORT", DARK_RED, msg)
def success(msg):    _emit("SUCCESS", GREEN, msg)
def exception(msg):  _emit("EXCEPTION", ORANGE, msg)

