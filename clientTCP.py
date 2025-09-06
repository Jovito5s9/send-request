import socket#adicionar threading pra melhorar
import threading

target_host='localhost'
target_port=8080
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send('* conectado no servidor'.encode())
print("-conectado")

def send_mensage():
    while True:
        mensage=input("- ")
        if(mensage.lower()=="sair"):
            break
        client.send(mensage.encode())

def recv_mensage():
    while True:
        try:
            data = client.recv(4096)
            if not data:
                print("* desconectou.")
                break
            print(f"\n{data.decode()}")
        except:
            break

threading.Thread(target=recv_mensage,daemon=True).start()
threading.Thread(target=send_mensage).start()