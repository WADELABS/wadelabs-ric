import sys
from pathlib import Path

# Ensure the package is in path if running as script
sys.path.append(str(Path(__file__).parent.parent))

from wadelabs_ric.ric.integrity_runner import main

if __name__ == "__main__":
    main()
