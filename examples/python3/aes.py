from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# AES Encryption
def aes_encrypt(key, plaintext):
    # Generate a random IV
    iv = os.urandom(16)

    # Create a Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create an encryptor
    encryptor = cipher.encryptor()

    # Pad the plaintext to ensure it's a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Encrypt the plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return iv, ciphertext

# AES Decryption
def aes_decrypt(key, iv, ciphertext):
    # Create a Cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create a decryptor
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext

# Main Function
if __name__ == "__main__":
    # Generate a random 256-bit AES key
    key = os.urandom(32)

    # Prompt user for the message to encrypt
    message = input("Enter the message you want to encrypt: ").encode('utf-8')

    # Encrypt the message
    iv, ciphertext = aes_encrypt(key, message)
    print("\nEncryption Key (hex):", key.hex())
    print("Initialization Vector (IV, hex):", iv.hex())
    print("Ciphertext (hex):", ciphertext.hex())

    # Decrypt the message
    decrypted_message = aes_decrypt(key, iv, ciphertext)
    print("\nDecrypted Message:", decrypted_message.decode('utf-8'))
