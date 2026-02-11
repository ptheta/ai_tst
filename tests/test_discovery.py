"""Test discovery module."""

import unittest
import time
from discovery import ServiceAnnouncer, discover_service, Server, discover_server


class TestDiscovery(unittest.TestCase):
    """Test server discovery."""

    def test_discover_service(self):
        """Test discovering server IP."""
        announcer = ServiceAnnouncer("127.0.0.1", 9001)
        announcer.start()
        time.sleep(0.2)
        
        result = discover_service(timeout=7)
        announcer.stop()
        
        self.assertIsNotNone(result)
        self.assertEqual(result["host"], "127.0.0.1")
        self.assertEqual(result["port"], 9001)

    def test_server_announces(self):
        """Test that server announces its IP."""
        server = Server(port=9002)
        server.start(host="127.0.0.1")
        time.sleep(0.2)
        
        result = discover_service(timeout=7)
        server.stop()
        
        self.assertIsNotNone(result)
        self.assertEqual(result["port"], 9002)

    def test_discover_server_function(self):
        """Test discover_server convenience function."""
        announcer = ServiceAnnouncer("192.168.1.100", 8000)
        announcer.start()
        time.sleep(0.2)
        
        result = discover_server(timeout=7)
        announcer.stop()
        
        self.assertIsNotNone(result)
        self.assertEqual(result["host"], "192.168.1.100")


if __name__ == "__main__":
    unittest.main()
