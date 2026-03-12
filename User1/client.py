# User1/client.py
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from crypto_utils import encrypt_aes, generate_aes_key
import base64

print("[Client] Loading keys...")

# Load your private key (User1)
with open('keys/your_private.pem', 'rb') as f:
    your_private_key = RSA.import_key(f.read())

# Load friend's public key (User2)
with open('keys/friend_public.pem', 'rb') as f:
    friend_public_key = RSA.import_key(f.read())

# Connect to server
print("[Client] Connecting to server...")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))
client.send(b"SENDER")
print("[Client] Connected!")

# Generate AES key and encrypt it with User2's public key
aes_key = generate_aes_key()
cipher_rsa = PKCS1_OAEP.new(friend_public_key)
encrypted_key = cipher_rsa.encrypt(aes_key)

# Send encrypted AES key
client.send(encrypted_key)
print("[Client] AES key sent!")
