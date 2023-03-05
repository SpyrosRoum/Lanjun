import os
import sys


def setup_path(root=".."):
    """Sets up the PYTHONPATH to be able to import from `lanjun`."""
    package = os.path.join(os.path.dirname(__file__), root)
    sys.path.insert(0, os.path.abspath(package))
