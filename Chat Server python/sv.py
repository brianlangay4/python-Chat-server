import tornado.ioloop
import tornado.web
import tornado.websocket

# List to hold connected clients
clients = []

class ChatHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("New client connected")
        clients.append(self)
        self.send_message_to_all("A new client has joined the chat")

    def on_message(self, message):
        print("Received message:", message)
        self.send_message_to_all(message)

    def on_close(self):
        print("Client disconnected")
        clients.remove(self)
        self.send_message_to_all("A client has left the chat")

    def send_message_to_all(self, message):
        for client in clients:
            if client != self:
                client.write_message(message)

def make_app():
    return tornado.web.Application([
        (r"/chat", ChatHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Chat server started")
    tornado.ioloop.IOLoop.current().start()
