#!/usr/bin/env python3
"""Build the primary self-contained Englewood Road field guide (Python + Pillow)."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parent / 'guide' / 'build.py'), run_name='__main__')
