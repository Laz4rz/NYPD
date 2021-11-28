"""
this is __init__ file of io_package package
"""

from .load import load_csv
from .save import save_csv

__all__ = ("load_csv", "save_csv")