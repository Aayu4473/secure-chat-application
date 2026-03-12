from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_aes_key():
    return get_random_bytes(16)  # 128-bit AES key

def encrypt_aes(key, data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext

def decrypt_aes(key, data):
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted.decode('utf-8')
