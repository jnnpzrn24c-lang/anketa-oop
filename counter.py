import socket
import time

NAME = input("Имя счётчика (например C1): ")
MY_PORT = int(input("Мой порт (например 5001): "))
MAIN_PORT = 5000
PRIORITY = int(input("Приоритет (чем больше, тем важнее): "))

PEERS = [("127.0.0.1", 5001), ("127.0.0.1", 5002)]
PEERS = [p for p in PEERS if p[1] != MY_PORT]

value = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", MY_PORT))
sock.settimeout(1.0)

print(f"[{NAME}] запущен на порту {MY_PORT}, приоритет {PRIORITY}")

while True:
    value += 1

    for ip, port in PEERS:
        try:
            sock.sendto(f"{NAME}:{value}".encode(), (ip, port))
        except Exception:
            pass

    try:
        sock.sendto(f"{NAME}:{PRIORITY}:{value}".encode(),
                    ("127.0.0.1", MAIN_PORT))
    except Exception:
        pass

    try:
        data, addr = sock.recvfrom(1024)
        print(f"[{NAME}] получил от {addr}: {data.decode()}")
    except socket.timeout:
        pass

    time.sleep(1)