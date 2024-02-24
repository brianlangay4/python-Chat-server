
## Chat Application Documentation

#Demo
![chatsv](https://github.com/brianlangay4/python-Chat-server/assets/67788456/96b69887-84bf-4288-99cc-90e63d9c83f2)



---


### Overview

This is a simple chat application implemented in Python using the Tornado web framework for the server-side and WebSocket for real-time communication between clients and the server.

### Components

1. **Server-side (chat_server.py):**
   - Responsible for handling client connections, receiving and relaying messages between clients.
   - Implemented using Tornado web framework.
   - Uses WebSocket protocol for real-time bidirectional communication.

2. **Client-side (chat_client.py):**
   - Allows users to connect to the chat server and send/receive messages.
   - Implemented using the `websocket-client` library for WebSocket communication.

### Server-side Implementation

- **ChatHandler Class:**
  - Inherits from `tornado.websocket.WebSocketHandler`.
  - Manages client connections, message reception, and relaying messages to other connected clients.
  - Methods:
    - `open`: Triggered when a new client connects. Adds the client to the list of connected clients and notifies all clients about the new connection.
    - `on_message`: Triggered when a client sends a message. Relays the message to all other connected clients.
    - `on_close`: Triggered when a client disconnects. Removes the client from the list of connected clients and notifies all clients about the disconnection.
    - `send_message_to_all`: Sends a message to all connected clients except the sender.

- **make_app Function:**
  - Creates a Tornado web application with the `ChatHandler` as the request handler.

- **Main Execution:**
  - Starts the Tornado web server to listen for incoming WebSocket connections on port 8888.

### Client-side Implementation

- **WebSocket Connection:**
  - Connects to the chat server using the WebSocket protocol.

- **Message Handling:**
  - Defines callback functions (`on_message`, `on_error`, `on_close`) to handle received messages, errors, and connection close events.

- **User Input:**
  - Starts a separate thread to continuously read user input and send messages to the server.

### Usage

1. **Server:**
   - Execute `python chat_server.py` to start the chat server.

2. **Client:**
   - Execute `python chat_client.py` to connect to the server and start sending/receiving messages.

### Dependencies

- Tornado web framework (`tornado`)
- WebSocket client library (`websocket-client`)

### Conclusion

This chat application provides a simple yet effective way for multiple clients to communicate with each other in real-time using a central server.

---
