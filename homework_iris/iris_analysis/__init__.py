"""
this is __init__ file of irys_analysis package
"""

from .io_package.load import load_csv
from .io_package.save import save_csv
from .calculate import  get_statistics

__all__ = ("load_csv", "save_csv", "get_statistics")
