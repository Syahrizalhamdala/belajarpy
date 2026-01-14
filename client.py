import socket
import threading

# Konfigurasi client
HOST = '127.0.0.1'
PORT = 555534

nickname = input("Masukkan nama Anda: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
except ConnectionRefusedError:
    print("Gagal terhubung ke server. Pastikan server sudah berjalan.")
    exit()

# Menerima pesan dari server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Koneksi terputus dari server.")
            client.close()
            break

# Mengirim pesan ke server
def write():
    while True:
        try:
            message = f'{nickname}: {input("")}'
            client.send(message.encode('utf-8'))
        except:
            print("Gagal mengirim pesan, koneksi terputus.")
            client.close()
            break

# Jalankan dua thread: satu untuk menerima, satu untuk menulis
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
