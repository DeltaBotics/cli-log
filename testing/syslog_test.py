import sys
from pathlib import Path

# Add the parent directory (root dir) to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

"""
# Testing Environment

Include test code below.
"""

import cli

def test_logging():
    try:
        # Configure logging to a file
        cli.logging.init(level=cli.logging.DEBUG, mode='w', handler_type='file', log_file_path='testing/test.log')

        cli.info('CLI started\nYo')
        cli.warn('Sup')
        cli.debug('I am a debug')
        cli.critical('Critical')

    except Exception as e:
        print(f"Exception occurred: {str(e)}")

if __name__ == "__main__":
    test_logging()

    cli.help()