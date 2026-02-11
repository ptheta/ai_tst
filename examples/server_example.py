"""
Example: Server that announces its IP on the network.

Run this, then run client_example.py in another terminal.
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from discovery import Server

if __name__ == "__main__":
    server = Server(port=9000)
    server.start(host="127.0.0.1")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping...")
        server.stop()
