"""Simple network discovery to find server IP on local network."""

import socket
import multiprocessing
import json
import time
from typing import Optional

DISCOVERY_PORT = 5555
DISCOVERY_BROADCAST = "255.255.255.255"


def _announce_process(host: str, port: int, status: str = "online"):
    """Announce server IP every 5 seconds."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    message = json.dumps({"host": host, "port": port, "status": status}).encode()

    try:
        while True:
            try:
                sock.sendto(message, (DISCOVERY_BROADCAST, DISCOVERY_PORT))
            except Exception as e:
                print(f"Announce error: {e}")
            time.sleep(5)
    except KeyboardInterrupt:
        pass
    finally:
        sock.close()


class ServiceAnnouncer:
    """Announces server IP on the local network via UDP broadcast."""

    def __init__(self, host: str, port: int, status: str = "online"):
        self.host = host
        self.port = port
        self.status = status
        self._process: Optional[multiprocessing.Process] = None

    def start(self):
        """Start announcing every 5 seconds in a separate process."""
        if self._process is not None:
            return
        
        self._process = multiprocessing.Process(
            target=_announce_process,
            args=(self.host, self.port, self.status),
            daemon=True
        )
        self._process.start()

    def stop(self):
        """Stop announcing."""
        if self._process:
            self._process.terminate()
            self._process.join(timeout=1)
            self._process = None


def discover_service(timeout: int = 5) -> Optional[dict]:
    """
    Listen for server IP announcement.
    
    Args:
        timeout: Seconds to wait
        
    Returns:
        Dict with {host, port} or None
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", DISCOVERY_PORT))
    sock.settimeout(timeout)

    try:
        data, _ = sock.recvfrom(4096)
        result = json.loads(data.decode())
        sock.close()
        return result
    except socket.timeout:
        sock.close()
        return None
    except Exception as e:
        print(f"Discovery error: {e}")
        sock.close()
        return None
