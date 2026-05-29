import os 
from cryptography.fernet import Fernet

def obtener_fernet():
    llave = os.getenv('CLAVE_SECRETA_FERNET')
    if not llave:
        raise ValueError("La variable de entorno 'CLAVE_SECRETA_FERNET' no está definida.")
    
    return Fernet(llave.encode())

def cifrar_texto(texto):
    f = obtener_fernet()
    texto_cifrado = f.encrypt(texto.encode())
    return texto_cifrado.decode()

def descifrar(texto_cifrado):
    f=obtener_fernet()
    texto = f.decrypt(texto_cifrado.encode())
    return texto.decode()