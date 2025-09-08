import socket
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))  # so pra descobrir a interface usada
ip_local = s.getsockname()[0]
s.close()

bind_ip = ip_local  #ip do server
bind_port = 8080       #porta do meu server

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#AF_NET=IP V6//SOCK_STREAM=protocolo TCP, juntos sao TCP/IP
server.bind((bind_ip,bind_port))
server.listen(5)
print ('[*] Escutando %s:%d ' %(bind_ip,bind_port))

def handle_recive(client_socket,addr):
    while True:
        try:
            request = client_socket.recv(1024)
            if not request:
                break
            print(f'*: %s' %request.decode())
        except:
            break
    client_socket.close()

def handle_send(client_socket, addr):
    while True:
        try:
            mensage = input("- ")      # input retorna str
            client_socket.send(f"*: {mensage}".encode())
        except:
            print("Erro ao enviar mensagem ou * desconectado.")
            break

def handle_client(client_socket,addr):
    threading.Thread(target=handle_recive,args=(client_socket,addr)).start()
    threading.Thread(target=handle_send,args=(client_socket,addr)).start()

while True:
    client, addr= server.accept()
    print('[*] Conexão aceita de: %s:%d' %(addr[0],addr[1]))
    client_handler= threading.Thread(target=handle_client,args=(client,addr))
    client_handler.start()