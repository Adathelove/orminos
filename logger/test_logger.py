import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# test_logger.py
from logger import info, debug, warn, fail, abort, success, exception

def main():
    info("This is an info message.")
    debug("This is a debug message.")
    warn("This is a warning.")
    fail("This is a failure event.")
    abort("This is an abort-condition message.")
    success("This is a success indicator.")
    exception("This is an exception-style message.")

if __name__ == "__main__":
    main()

