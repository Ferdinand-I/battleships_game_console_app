import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected: ', addr)

while True:
    data = conn.recv(1024)
    if not data:
        continue
    with open(file='data.txt', mode='w') as f:
        f.write(str(data))
        f.close()

conn.close()
