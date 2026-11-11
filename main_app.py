import socket
import time

MAIN_PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", MAIN_PORT))
sock.settimeout(1.0)

counters = {}

print("[MAIN] запущена, жду данные от счётчиков...")

while True:
    try:
        data, addr = sock.recvfrom(1024)
        name, priority, value = data.decode().split(":")
        counters[name] = {
            "priority": int(priority),
            "value": int(value),
            "last_seen": time.time(),
        }
    except socket.timeout:
        pass
    except Exception as e:
        print("Ошибка разбора:", e)

    now = time.time()
    alive = {n: d for n, d in counters.items()
             if now - d["last_seen"] <= 3}

    if alive:
        best = max(alive.items(), key=lambda kv: kv[1]["priority"])
        name, d = best
        print(f"[MAIN] активных: {list(alive)} | "
              f"приоритетный: {name} = {d['value']}")
    else:
        print("[MAIN] нет живых счётчиков")