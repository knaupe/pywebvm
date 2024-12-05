from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

# Generate RSA Key Pair
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()  # Explicit backend for older versions
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Serialize Private Key
def serialize_private_key(private_key):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem

# Serialize Public Key
def serialize_public_key(public_key):
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem

# Encrypt Message
def encrypt_message(public_key, message):
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

# Decrypt Message
def decrypt_message(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

# Main Function
if __name__ == "__main__":
    # Generate keys
    private_key, public_key = generate_rsa_keys()

    # Serialize and display keys
    private_pem = serialize_private_key(private_key)
    public_pem = serialize_public_key(public_key)
    print("Private Key:\n", private_pem.decode('utf-8'))
    print("Public Key:\n", public_pem.decode('utf-8'))

    # Prompt user for the message to encrypt
    message = input("\nEnter the message you want to encrypt: ").encode('utf-8')

    # Encrypt the message
    ciphertext = encrypt_message(public_key, message)
    print("\nCiphertext (hex):\n", ciphertext.hex())

    # Decrypt the message
    decrypted_message = decrypt_message(private_key, ciphertext)
    print("\nDecrypted Message:\n", decrypted_message.decode('utf-8'))
