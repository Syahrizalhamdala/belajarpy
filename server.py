import socket
import threading

# Konfigurasi server
HOST = '127.0.0.1'   # alamat lokal
PORT = 55555         # port bebas

# Membuat socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []  # Menyimpan semua koneksi client
nicknames = []  # Menyimpan nama pengguna

# Fungsi broadcast ke semua client
def broadcast(message, _client=None):
    for client in clients:
        if client != _client:  # jangan kirim balik ke pengirim
            try:
                client.send(message)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

# Fungsi menangani pesan dari tiap client
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!\n".encode('utf-8'))
            nicknames.remove(nickname)
            break

# Menerima koneksi client baru
def receive():
    print(f"Server berjalan di {HOST}:{PORT}")
    while True:
        client, address = server.accept()
        print(f"Terhubung dengan {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname client: {nickname}")
        broadcast(f"{nickname} bergabung ke chat!\n".encode('utf-8'))
        client.send("Terhubung ke server!\n".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
