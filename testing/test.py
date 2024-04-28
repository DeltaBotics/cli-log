import sys
from pathlib import Path

# Add the parent directory (root dir) to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

"""
# Testing Environement

Include test code below.
"""

import cli

cli.info("Hello world!")
cli.add(severity="Testing", message="Hello", prefix="test", color=cli.MAGENTA)

cli.init(log_format="[{time} ! {severity}]{prefix} {message}", reset=True)

cli.error("Error between error raising.")

cli.init(reset=True) # Doesn't do anything because we didnt set format before

cli.debug("Should not get executed.")