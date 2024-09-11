import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

# Función para leer la clave privada desde un archivo PEM
def load_private_key(pem_file):
    with open(pem_file, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,  # Sin contraseña
            backend=default_backend()
        )
    return private_key

# Desencriptar un mensaje usando la clave privada con un padding específico
def decrypt_message(private_key, ciphertext, pad):
    decrypted_message = private_key.decrypt(
        ciphertext,
        pad
    )
    return decrypted_message

# Leer la clave privada
private_key = load_private_key("new_private_key.pem")

# Texto cifrado que te han dado (en base64)
encrypted_message_base64 = "ozqu8DguOT4zppalpv2aGIColztrOc1qpUdvkbYuCJkohPnO2ATcTvPoUrVutQR7zg1gf9cYTwLSOiazaZTlp7efHapB5+kEFP5OpphFXECGwigM6IdgaZqUf+KGW/W2bPKhvyWcUqwED4O9v9WzknnBQBGbKrG1BEO5/FXNNrpUA788psYgOFhZPKFU/9mVacTIz9J1G+nr7PZyLmN1R5p1R06uFN9Z79c9mFTgEqAY3BbxSgYHuIupXPPs3QrPjgdBdRueI/4YLOBzARWVOvNG3Pltds7u6RrYYMqibdxVjiZAz4LWnLJM+Lz/prFTaYtU4J3AgQSBU1E0Uknu4w=="

# Decodificar el mensaje en base64 a bytes
encrypted_message = base64.b64decode(encrypted_message_base64)

# Intentar desencriptar con OAEP
try:
    decrypted_message = decrypt_message(private_key, encrypted_message, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    print(f"Mensaje desencriptado con OAEP: {decrypted_message.decode()}")
except ValueError:
    print("Desencriptación con OAEP fallida.")

# Intentar desencriptar con PKCS1v15
try:
    decrypted_message = decrypt_message(private_key, encrypted_message, padding.PKCS1v15())
    print(f"Mensaje desencriptado con PKCS1v15: {decrypted_message.decode()}")
except ValueError:
    print("Desencriptación con PKCS1v15 fallida.")
