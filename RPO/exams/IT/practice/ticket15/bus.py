import time
import threading
import random

class Bus:
    def __init__(self):
        self.messages = []
        self.lock = threading.Lock()

    def send_message(self, message, sender):
        with self.lock:
            print(f"{sender} отправляет сообщение: '{message}'")
            self.messages.append((message, sender))
            time.sleep(1)

    def receive_messages(self):
        with self.lock:
            if self.messages:
                for message, sender in self.messages:
                    print(f"{sender} получил сообщение: '{message}'")
                self.messages.clear()

class Node:
    def __init__(self, name, bus):
        self.name = name
        self.bus = bus

    def send_message(self):
        message = f"Сообщение от {self.name}"
        self.bus.send_message(message, self.name)

    def listen(self):
        while True:
            self.bus.receive_messages()
            time.sleep(2)

def main():
    num_nodes = int(input("Введите количество узлов в сети с общей шиной: "))
    bus = Bus()
    nodes = [Node(f"Узел {i + 1}", bus) for i in range(num_nodes)]

    for node in nodes:
        threading.Thread(target=node.listen, daemon=True).start()
    for _ in range(5):
        random_node = random.choice(nodes)
        threading.Thread(target=random_node.send_message, daemon=True).start()
        time.sleep(1)

    time.sleep(10)


if __name__ == "__main__":
    main()
