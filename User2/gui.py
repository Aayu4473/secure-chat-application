print("[STEP 1] GUI script started")

from tkinter import *
import threading
from client import client, aes_key
from crypto_utils import encrypt_aes, decrypt_aes


print("[STEP 2] Imported all modules")

# Function to send messages
def send_message():
    global aes_key
    if not aes_key:
        print("❌ AES key not set yet. Cannot send message.")
        return

    print("[STEP 3] Sending message")
    msg = message_entry.get()
    if msg:
        encrypted = encrypt_aes(aes_key,msg)
        client.send(encrypted)
        chat_window.insert(END, "You: " + msg + "\n")
        message_entry.delete(0, END)
        threading.Thread(target=auto_delete, args=(chat_window.index("end-2c linestart"),), daemon=True).start()


# Function to receive and decrypt incoming messages
def receive_messages():
    global aes_key
    while True:
        try:
            encrypted_msg = client.recv(1024)
            if encrypted_msg and aes_key:
                decrypted_msg = decrypt_aes(aes_key, encrypted_msg)
                chat_window.insert(END, "Friend: " + decrypted_msg + "\n")
                threading.Thread(target=auto_delete, args=(chat_window.index("end-2c linestart"),), daemon=True).start()
        except:
            break

# Self-destruct message
def auto_delete(index):
    print("[STEP 4] Starting self-destruct timer")
    import time
    time.sleep(5)
    chat_window.delete(index, f"{index}+1line")



# GUI setup
print("[STEP 5] Setting up GUI window")
root = Tk()
root.title("User2 - Secure Chat")
root.geometry("400x400")

chat_window = Text(root, height=20, width=50)
chat_window.pack()

message_entry = Entry(root, width=40)
message_entry.pack(pady=10)

send_button = Button(root, text="Send", command=send_message)
send_button.pack()

print("[STEP 6] Launching GUI window")
root.mainloop()


