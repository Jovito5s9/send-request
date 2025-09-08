import socket
import threading

rede = ""
ativos = []
lock = threading.Lock()

def ip_generico():
    global rede
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
    except Exception:
        ip_local = socket.gethostbyname(socket.gethostname())
    finally:
        try: s.close()
        except: pass

    pos = ip_local.rfind('.')
    rede = ip_local[:pos+1]

def testar_ip(ip, port=8080, timeout=0.5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        if sock.connect_ex((ip, port)) == 0:
            with lock:
                ativos.append(ip)
    except Exception as e:
        print(f"erro {ip}: {e}")
        pass
    finally:
        sock.close()

def ips():
    global ativos
    ativos = []
    ip_generico()
    threads = []
    for i in range(1, 255):
        ip = rede + str(i)
        t = threading.Thread(target=testar_ip, args=(ip,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    return ativos

if __name__ == "__main__":#pra rodar so aq e nn no meu chat
    print(ips())
