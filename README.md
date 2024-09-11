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

![image](https://github.com/user-attachments/assets/6b6b4b3f-8669-4f06-a81a-368afeec59a1)



Respuesta cambiando el padding al desencriptar:


![image](https://github.com/user-attachments/assets/59f2d669-e574-4e0f-a974-231020f73cb9)



## main2.py (Desencriptación con la llave privada de ustedes )

En este caso solo tengo el texto a desencriptar e intento con los 2 padding y no funciona.

![image](https://github.com/user-attachments/assets/39b45433-692e-450b-9885-dd3f0b3f1112)


#### Respuesta:

![image](https://github.com/user-attachments/assets/8eaf8918-5335-47b0-bcad-f1f60bbb20a4)




Eso usando la llave privada  `private_key = load_private_key("new_private_key.pem")` que está en el formato `PKCS#1`.

Si uso la llave privada `new_private_key_pkcs8` que está en formato `PKCS#8` tampoco funciona.

<img width="573" alt="image" src="https://gist.github.com/user-attachments/assets/ca185a06-09b1-4740-9691-cd2e2049b1d9">
