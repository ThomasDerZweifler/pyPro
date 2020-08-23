import socket

# (base) ➜  network git:(master) ✗ python Server.py
# [127.0.0.1] Hello
# Antwort: "Huhu"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 50000)) 
s.listen(1)
try: 
    while True: 
        komm, addr = s.accept()
        while True: 
            data = komm.recv(1024) 
            if not data: 
                komm.close()
                break
            print("[{}] {}".format(addr[0], data.decode())) 
            nachricht = input("Antwort: ")
            komm.send(nachricht.encode()) 
finally: 
    s.close()