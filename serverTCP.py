import socket
import threading

bind_ip = 'localhost'  #nome do server
bind_port = 8080       #porta do meu server

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#AF_NET=IP V6//SOCK_STREAM=protocolo TCP
server.bind((bind_ip,bind_port))
server.listen(5)
print ('[*] Escutando %s:%d ' %(bind_ip,bind_port))

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print('[*] Recebido: %s' %request.decode())
    print('\n---------------------\n')
    client_socket.send(('\nMensagem destinada ao cliente: %s\n' %addr[0]).encode())
    client_socket.send(('\n ACK! \nRecebido pelo servidor!\n').encode())#cliente recebeu a mensagem
    client_socket.close()

while True:
    client, addr= server.accept()
    print('[*] Conexão aceita de: %s:%d' %(addr[0],addr[1]))
    client_handler= threading.Thread(target=handle_client,args=(client,))
    client_handler.start()