# Python Server IP Discovery

Ultra-simple network discovery: servers announce their IP on the local network, clients discover it.

## Quick Start

**Server** - auto-detects and announces its IP every 5 seconds:
```python
from discovery import Server
import socket

def get_local_ip():
    """Auto-detect local IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

server = Server(port=9000)
server.start(host=get_local_ip())
```

Or run the example which does this automatically:
```bash
python examples/server_example.py
```

**Client** - discovers server IP:
```python
from discovery import discover_server

result = discover_server(timeout=5)
print(result)  # {'host': '192.168.1.100', 'port': 9000}
```

## How It Works

- Server announces `{host, port}` via UDP broadcast on port 5555 every 5 seconds
- Server auto-detects its local IP address on network interface

- Client listens on port 5555 and receives the announcement
- Returns immediately with server's IP

## API

**Server**
- `Server(port)` - Create server
- `start(host)` - Start announcing this IP
- `stop()` - Stop announcing

**Client**
- `discover_server(timeout=5)` - Wait for server announcement, returns `{host, port}` or None
- `discover_service(timeout=5)` - Same as above

## Example

Terminal 1:
```bash
python examples/server_example.py
```

Terminal 2:
```bash
python examples/client_example.py
```

## Testing

```bash
python -m pytest tests/test_discovery.py -v
```



