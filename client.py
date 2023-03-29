import socket

def cesar_cipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

HOST = '127.0.0.1'  
PORT = 8000       

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    mensaje = input('Ingrese el mensaje a enviar: ')
    encriptar = input('¿Desea encriptar el mensaje? (si/no): ')
    if encriptar == 'si':
        llave = int(input('Ingrese la llave para encriptar (1-28): '))
        mensaje_encriptado = cesar_cipher(mensaje, llave)
        s.sendall(mensaje_encriptado.encode('utf-8'))
        print('Mensaje enviado encriptado:', mensaje_encriptado)
    else:
        s.sendall(mensaje.encode('utf-8'))
        print('Mensaje enviado sin encriptar:', mensaje)
