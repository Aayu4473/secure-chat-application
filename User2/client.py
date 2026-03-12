# User2/client.py
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from crypto_utils import encrypt_aes, decrypt_aes # Make sure this file exists in same folder or path
import base64

print("[Client] Loading keys...")

# Load your private key (User2)
with open('keys/your_private.pem', 'rb') as f:
    your_private_key = RSA.import_key(f.read())

# Load friend's public key (User1)
with open('keys/friend_public.pem', 'rb') as f:
    friend_public_key = RSA.import_key(f.read())

# Connect to server
print("[Client] Connecting to server...")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))
client.send(b"RECEIVER")
print("[Client] Connected!")

# Receive encrypted AES key from sender
print("[Client] Waiting for AES key...")
encrypted_key = client.recv(256)
cipher_rsa = PKCS1_OAEP.new(your_private_key)
aes_key = cipher_rsa.decrypt(encrypted_key)
print("[Client] AES key received!")


