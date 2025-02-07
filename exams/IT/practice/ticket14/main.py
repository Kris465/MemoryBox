import socket
import os
from subprocess import Popen, PIPE

def get_host_ip(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror as e:
        print(f"Не удалось получить IP-адрес для {hostname}: {e}")
        return None

def ping_host(hostname):
    if os.name == 'nt':
        command = ["ping", "-n", "1", hostname]
    else:
        command = ["ping", "-c", "1", hostname]
    
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    
    if process.returncode == 0:
        print("Хост доступен.")
    else:
        print("Ошибка при пинге:", error.decode().strip())

def trace_route(hostname):
    if os.name == 'nt':
        command = ["tracert", hostname]
    else:
        command = ["traceroute", hostname]
    
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    
    if process.returncode == 0:
        print("Результаты трассировки:")
        print(output.decode().strip())
    else:
        print("Ошибка при трассировке маршрута:", error.decode().strip())

def main():
    hostname = input("Введите имя хоста или IP-адрес: ").strip()
    
    ip_address = get_host_ip(hostname)
    if ip_address:
        print(f"IP-адрес: {ip_address}")
        
        ping_host(hostname)
        trace_route(hostname)


if __name__ == "__main__":
    main()
