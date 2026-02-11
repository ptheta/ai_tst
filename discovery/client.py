"""Client that discovers server IP on the network."""

from discovery.discoverer import discover_service


def discover_server(timeout: int = 5) -> dict:
    """
    Discover server IP on the local network.
    
    Args:
        timeout: Seconds to wait
        
    Returns:
        Dict with {host, port} or None
    """
    return discover_service(timeout)
