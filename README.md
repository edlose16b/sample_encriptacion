# Usando Python:


## main.py ( encriptación y desencriptación con mi llave publcia y privada  )
en main.py hago uso de la llave publica y privada para encriptar y desencriptar el texto.

```python

# Encriptar un mensaje usando la clave pública
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

# Desencriptar un mensaje usando la clave privada
def decrypt_message(private_key, ciphertext):
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message

# Mensaje a encriptar
message = b"Hola amigos"

# Encriptar el mensaje
encrypted_message = encrypt_message(public_key, message)
print(f"Mensaje encriptado: {encrypted_message}")

# Desencriptar el mensaje
decrypted_message = decrypt_message(private_key, encrypted_message)
print(f"Mensaje desencriptado: {decrypted_message.decode()}")

```

Como ven el padding es `padding.MGF1(algorithm=hashes.SHA256())`

y si cambio el padding en la desencriptación, luego falla.
Si cambio el algirtmo de encriptación en el padding `OAEP`, también falla.

Por eso seria bueno que también de su lado confirmen como es que andan encriptando.


#### Respuesta:

<img width="734" alt="image" src="https://gist.github.com/user-attachments/assets/509ce176-43be-43af-847c-68c6d8fae56c">


Respuesta cambiando el padding al desencriptar:


<img width="734" alt="image" src="https://gist.github.com/user-attachments/assets/189b6f41-e2b6-47f9-befd-3a0066771033">


## main2.py (Desencriptación con la llave privada de ustedes )

En este caso solo tengo el texto a desencriptar e intento con los 2 padding y no funciona.

<img width="787" alt="image" src="https://gist.github.com/user-attachments/assets/c0e06c21-61f0-4ee6-a8b5-40f809bb9ca1">

#### Respuesta:

<img width="508" alt="image" src="https://gist.github.com/user-attachments/assets/e21de614-d3a2-445f-af2c-eff2527b769c">



Eso usando la llave privada  `private_key = load_private_key("new_private_key.pem")` que está en el formato `PKCS#1`.

Si uso la llave privada `new_private_key_pkcs8` que está en formato `PKCS#8` tampoco funciona.

<img width="573" alt="image" src="https://gist.github.com/user-attachments/assets/ca185a06-09b1-4740-9691-cd2e2049b1d9">
