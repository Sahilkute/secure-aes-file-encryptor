from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

AES_KEY = os.environ.get("AES_KEY", b"ThisIsA16ByteKey")  # Must be 16 bytes for AES-128

def encrypt_file(data, key=AES_KEY):
    backend = default_backend()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    # Padding
    padding_len = 16 - len(data) % 16
    data += bytes([padding_len]) * padding_len

    encrypted = encryptor.update(data) + encryptor.finalize()
    return iv + encrypted  # Prepend IV for use in decryption

def decrypt_file(encrypted_data, key=AES_KEY):
    backend = default_backend()
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding
    padding_len = decrypted[-1]
    return decrypted[:-padding_len]
