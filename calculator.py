"""
UML Calculator - Community Edition Launcher
"""
import os
import sys
from pathlib import Path

# Get the absolute path to the project root
PROJECT_ROOT = Path(__file__).parent.absolute()

# Add the project root to sys.path
sys.path.insert(0, str(PROJECT_ROOT))

# Import and run the CLI
try:
    from ui.modern_cli import app
    
    if __name__ == "__main__":
        print(f"UML Calculator Community Edition")
        app()
except ImportError as e:
    print(f"Error loading UML Calculator: {e}")
    print(f"Current path: {PROJECT_ROOT}")
    print("Please make sure you've installed all required dependencies:")
    print("  pip install -r requirements.txt")
    sys.exit(1)
