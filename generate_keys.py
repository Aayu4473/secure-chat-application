from Crypto.PublicKey import RSA
import os

def save_key_pair(folder, private_filename, public_filename):
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Create folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    with open(os.path.join(folder, private_filename), 'wb') as f:
        f.write(private_key)

    with open(os.path.join(folder, public_filename), 'wb') as f:
        f.write(public_key)

    return key

print("🔐 Generating RSA keys for User1 and User2...")

# Generate User1 keys
user1_folder = 'User1/keys'
user1_private = 'your_private.pem'
user1_public = 'your_public.pem'
user1_key = save_key_pair(user1_folder, user1_private, user1_public)

# Generate User2 keys
user2_folder = 'User2/keys'
user2_private = 'your_private.pem'
user2_public = 'your_public.pem'
user2_key = save_key_pair(user2_folder, user2_private, user2_public)

# Now copy each other's public key
with open(os.path.join(user2_folder, user2_public), 'rb') as f:
    user2_pub = f.read()
with open(os.path.join(user1_folder, 'friend_public.pem'), 'wb') as f:
    f.write(user2_pub)

with open(os.path.join(user1_folder, user1_public), 'rb') as f:
    user1_pub = f.read()
with open(os.path.join(user2_folder, 'friend_public.pem'), 'wb') as f:
    f.write(user1_pub)

print("✅ All keys generated successfully!")
print("📁 User1/keys/: your_private.pem, your_public.pem, friend_public.pem")
print("📁 User2/keys/: your_private.pem, your_public.pem, friend_public.pem")
