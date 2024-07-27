import sys
import os

# Add the parent directory of the 'modules' directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))