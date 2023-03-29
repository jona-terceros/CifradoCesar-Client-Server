import socket

def cesar_decipher(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

HOST = '127.0.0.1'  
PORT = 8000        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('El servidor está esperando conexiones...')
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            print('Mensaje recibido:', data)
            desencriptar = input('¿Desea desencriptar el mensaje? (si/no): ')
            if desencriptar == 'si':
                llave = int(input('Ingrese la llave para desencriptar (1-28): '))
                mensaje_desencriptado = cesar_decipher(data, -llave)
                print('Mensaje desencriptado:', mensaje_desencriptado)
            else:
                print('Mensaje sin desencriptar:', data)
