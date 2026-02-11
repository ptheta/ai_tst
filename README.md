# Python Server IP Discovery

Ultra-simple network discovery: servers announce their IP on the local network, clients discover it.

## Quick Start

**Server** - announces its IP every 1 second:
```python
from discovery import Server

server = Server(port=9000)
server.start(host="192.168.1.100")
```

**Client** - discovers server IP:
```python
from discovery import discover_server

result = discover_server(timeout=5)
print(result)  # {'host': '192.168.1.100', 'port': 9000}
```

## How It Works

- Server announces `{host, port}` via UDP broadcast on port 5555 every second
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



