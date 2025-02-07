import platform
import socket


def get_system_info():
    # Получение информации о системе
    system = platform.system()
    release = platform.release()
    version = platform.version()

    return f"Система: {system}\nВерсия системы: {release}\nВерсия сборки: {version}"


def get_network_interfaces():
    # Получение списка всех сетевых интерфейсов
    interfaces = []
    for interface in socket.if_nameindex():
        name = interface[1]
        try:
            ip_address = socket.gethostbyname(name)
            interfaces.append(f"Интерфейс: {name}, IP-адрес: {ip_address}")
        except Exception as e:
            print(f"Ошибка получения IP для интерфейса {name}: {e}")

    return "\n".join(interfaces)


if __name__ == "__main__":
    # Вывод информации о системе
    print(get_system_info())

    # Вывод информации о сетевых интерфейсах
    print("\nСетевые интерфейсы:")
    print(get_network_interfaces())
