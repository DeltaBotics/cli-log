import sys
from pathlib import Path

# Add the parent directory (root dir) to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

"""
# Testing Environment

Include test code below.
"""

from cli import logging

def test_logging():
    try:
        # Configure logging to a file
        log = logging.init(level=logging.DEBUG, mode='a', handler_type='file', log_file_path='best.log')

        # Log some messages
        log.debug('Debug message')
        log.info('Info message')
        log.warning('Warning message')
        log.error('Error message')
        log.critical('Critical message')

    except Exception as e:
        print(f"Exception occurred: {str(e)}")

if __name__ == "__main__":
    test_logging()