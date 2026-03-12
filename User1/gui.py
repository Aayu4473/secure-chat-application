import tkinter as tk
import threading
import time
from client import client, aes_key
from crypto_utils import encrypt_aes, decrypt_aes

def send_msg():
    msg = entry.get()
    entry.delete(0, tk.END)
    encrypted = encrypt_aes(aes_key,msg)
    client.send(encrypted)
    add_msg("You", msg, self_destruct=True)

def receive_msg():
    while True:
        try:
            data = client.recv(4096)
            message = decrypt_aes(aes_key,data)
            add_msg("Friend", message)
        except Exception as e:
            print("[Error receiving message]:", e)
            break

def add_msg(sender, msg, self_destruct=False):
    chat_area.insert(tk.END, f"{sender}: {msg}\n")
    if self_destruct:
        threading.Thread(target=auto_delete, args=(msg,), daemon=True).start()

def auto_delete(msg):
    time.sleep(5)
    content = chat_area.get("1.0", tk.END)
    updated_content = content.replace(f"You: {msg}\n", "")
    chat_area.delete("1.0", tk.END)
    chat_area.insert(tk.END, updated_content)

root = tk.Tk()
root.title("User 1 - Secure Chat")
root.geometry("400x500")

chat_area = tk.Text(root, wrap="word", font=("Arial", 12))
chat_area.pack(pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(fill=tk.X, padx=10)

send_btn = tk.Button(root, text="Send", command=send_msg)
send_btn.pack(pady=5)

threading.Thread(target=receive_msg, daemon=True).start()

root.mainloop()
