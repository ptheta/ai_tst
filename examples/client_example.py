"""
Example: Discover server IP on the network.

Run server first in another terminal:
    python examples/server_example.py

Then run this:
    python examples/client_example.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from discovery import discover_server

if __name__ == "__main__":
    server_info = discover_server(timeout=5)
    
    if server_info:
        print(f"Found server at {server_info['host']}:{server_info['port']}")
    else:
        print("No server found")
