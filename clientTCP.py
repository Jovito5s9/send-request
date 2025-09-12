import socket#adicionar threading pra melhorar
import threading
from ipUDP import ips

target_host=''
target_port=8080
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def escolher_servidor():
    global target_host
    options = ips() 
    if not options:
        print("Nenhum chat disponivel.")
        return None
    print("você deseja se conectar com quem?")
    for opc, ip in enumerate(options, start=1):
        print(f"{opc} - ip: {ip}")
    print("(pressione Enter ou qualquer outra tecla para sair)")
    escolha = input("Escolha o número: ").strip()
    try:
        option = int(escolha)
    except ValueError:
        print("Saindo.")
        return None
    if 1 <= option <= len(options):
        target_host = options[option-1]
        print("Selecionado:", target_host)
    else:
        print("Número fora do intervalo.")
        return None


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

def cliente():
    escolher_servidor()
    try:
        client.connect((target_host,target_port))
        client.send('* conectado no servidor'.encode())
        print("-conectado")

        threading.Thread(target=recv_mensage,daemon=True).start()
        threading.Thread(target=send_mensage).start()
    except:
        return None
if __name__=='__main__':
    cliente()