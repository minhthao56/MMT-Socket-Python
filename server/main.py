import socket
from functions.AppRuning import handleGetListRunning


SERVER_PORT = 65432
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = "utf8"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, SERVER_PORT))
server.listen()

print("server:", HOST, SERVER_PORT)
print("Waiting for Client")

try:
    conn, addr = server.accept()
    print("Client", addr, "connected")
    print("conn:", conn.getsockname())
    msg = None
    while (msg != "x"):
        msg = conn.recv(20000).decode(FORMAT)
        print("client ", addr, "says", msg)
        if(msg == "check"):
            conn.sendall("connected".encode(FORMAT))
        if(msg == "running-app"):
            listJOSN = handleGetListRunning()
            conn.sendall(listJOSN.encode(FORMAT))


except:
    print("Error")


print("End")
input()
conn.close()
