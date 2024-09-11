from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Función para leer la clave pública desde un archivo PEM
def load_public_key(pem_file):
    with open(pem_file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

# Función para leer la clave privada desde un archivo PEM
def load_private_key(pem_file):
    with open(pem_file, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,  # Sin contraseña
            backend=default_backend()
        )
    return private_key

# Encriptar un mensaje usando la clave pública
def encrypt_message(public_key, message):
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    return ciphertext

# Desencriptar un mensaje usando la clave privada
def decrypt_message(private_key, ciphertext):
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    return decrypted_message

# Leer claves
public_key = load_public_key("company_public.pem")
private_key = load_private_key("company_private_unencrypted.pem")

# Mensaje a encriptar
message = b"Hola amigos"

# Encriptar el mensaje
encrypted_message = encrypt_message(public_key, message)
print(f"Mensaje encriptado: {encrypted_message}")

# Desencriptar el mensaje
decrypted_message = decrypt_message(private_key, encrypted_message)
print(f"Mensaje desencriptado: {decrypted_message.decode()}")
