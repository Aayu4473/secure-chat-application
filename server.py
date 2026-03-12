import socket
import threading

clients = []
sender = None
receiver = None

def main():
    global sender, receiver

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen(2)
    print("[SERVER] Listening on port 9999...")

    while True:
        conn, addr = server.accept()
        print(f"[SERVER] Connected by {addr}")

        # First message from client should say its role: "SENDER" or "RECEIVER"
        role = conn.recv(1024).decode()
        print(f"[SERVER] Role received: {role}")

        if role == "SENDER":
            sender = conn
            print("[SERVER] Sender connected.")
        elif role == "RECEIVER":
            receiver = conn
            print("[SERVER] Receiver connected.")
        else:
            print("[SERVER] Unknown role. Closing connection.")
            conn.close()
            continue

        # When both are connected, receive AES key from sender and send to receiver
        if sender and receiver:
            print("[SERVER] Waiting for encrypted AES key from sender...")
            encrypted_key = sender.recv(256)
            print("[SERVER] Received AES key from sender.")
            receiver.send(encrypted_key)
            print("[SERVER] Sent AES key to receiver.")

            # Start threads to relay chat messages between sender and receiver
            threading.Thread(target=forward_messages, args=(sender, receiver)).start()
            threading.Thread(target=forward_messages, args=(receiver, sender)).start()

def forward_messages(source, destination):
    while True:
        try:
            msg = source.recv(4096)
            if not msg:
                break
            destination.sendall(msg)
        except:
            break

    source.close()
    destination.close()
    print("[SERVER] A client has disconnected.")

if __name__ == "__main__":
    main()
