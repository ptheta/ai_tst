"""Server that announces its IP on the network."""

from discovery.discoverer import ServiceAnnouncer


class Server:
    """Server that announces its IP via UDP broadcast."""

    def __init__(self, port: int = 9000):
        self.port = port
        self._announcer = None

    def start(self, host: str = "127.0.0.1", status: str = "online"):
        """Start announcing this server's IP on the network."""
        self._announcer = ServiceAnnouncer(host, self.port, status)
        self._announcer.start()
        print(f"Server announcing at {host}:{self.port}")

    def stop(self):
        """Stop announcing."""
        if self._announcer:
            self._announcer.stop()
