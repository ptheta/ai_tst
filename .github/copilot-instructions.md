# Copilot Instructions

## Project Overview
Ultra-simple IP discovery library. Servers announce their IP via UDP broadcast on port 5555, clients listen and retrieve it. No TCP communication or complex state management.

## How It Works

**Server Side:**
```python
from discovery import Server
server = Server(port=9000)
server.start(host="192.168.1.100")  # Broadcasts UDP every 1 second
```

**Client Side:**
```python
from discovery import discover_server
info = discover_server(timeout=5)  # Returns {host, port} or None
```

## Architecture

Two simple functions:
1. `ServiceAnnouncer(host, port)` - UDP broadcast sender
2. `discover_service(timeout)` - UDP broadcast receiver

That's it. No connection management, no state tracking.

## Code Structure

| File | Purpose |
|------|---------|
| `discovery/discoverer.py` | `ServiceAnnouncer`, `discover_service()` |
| `discovery/server.py` | `Server` wrapper class |
| `discovery/client.py` | `discover_server()` convenience function |
| `examples/server_example.py` | Basic server announcing |
| `examples/client_example.py` | Basic client discovering |
| `tests/test_discovery.py` | Simple unit tests |

## Conventions

- **Port 5555**: UDP discovery channel (edit `DISCOVERY_PORT` constant to change)
- **Message format**: JSON `{host, port}` only
- **Thread safety**: All I/O in daemon threads, safe to call from anywhere
- **Cleanup**: Use `stop()` method to close sockets cleanly

## Testing

```bash
python -m pytest tests/test_discovery.py -v
```

## Key Points

- No TCP server needed - just UDP broadcast + listen
- No dependencies - stdlib only
- LAN-only - broadcast doesn't cross routers
- Fire-and-forget - announcements continue until `stop()` called





