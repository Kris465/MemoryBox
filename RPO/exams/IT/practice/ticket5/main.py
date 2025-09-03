import platform
import socket

def get_system_info():
    system_info = {
        'Операционная система': platform.system(),
        'Версия ОС': platform.version(),
        'Имя компьютера': platform.node(),
        'Архитектура': platform.architecture()[0],
        'Процессор': platform.processor(),
        'Python версия': platform.python_version()
    }
    return system_info

def get_network_interfaces():
    interfaces = socket.getaddrinfo(socket.gethostname(), None)
    network_info = {}
    
    for interface in interfaces:
        family, socktype, proto, canonname, sockaddr = interface
        ip_address = sockaddr[0]
        if ip_address not in network_info:
            network_info[ip_address] = {
                'family': family,
                'socktype': socktype,
                'proto': proto,
                'canonical_name': canonname
            }
    
    return network_info

def print_system_info(system_info):
    print("Основные данные о системе:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

def print_network_interfaces(network_info):
    print("\nСетевые интерфейсы:")
    for ip, details in network_info.items():
        print(f"IP-адрес: {ip}")
        print(f"  Семейство: {details['family']}")
        print(f"  Тип сокета: {details['socktype']}")
        print(f"  Протокол: {details['proto']}")
        print(f"  Каноническое имя: {details['canonical_name']}\n")

def main():
    system_info = get_system_info()
    network_info = get_network_interfaces()
    
    print_system_info(system_info)
    print_network_interfaces(network_info)


if __name__ == "__main__":
    main()
