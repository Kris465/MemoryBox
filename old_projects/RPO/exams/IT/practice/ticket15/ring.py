import time
import threading

class Node:
    def __init__(self, name):
        self.name = name
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node

    def send_message(self, message):
        print(f"{self.name} отправляет сообщение: '{message}'")
        time.sleep(1)
        if self.next_node:
            self.next_node.receive_message(message)

    def receive_message(self, message):
        print(f"{self.name} получил сообщение: '{message}'")
        self.process_message(message)

    def process_message(self, message):
        print(f"{self.name} обрабатывает сообщение: '{message}'")
        self.send_message(message)

def create_ring(num_nodes):
    nodes = [Node(f"Узел {i + 1}") for i in range(num_nodes)]
    for i in range(num_nodes):
        nodes[i].set_next_node(nodes[(i + 1) % num_nodes])
    return nodes

def main():
    num_nodes = int(input("Введите количество узлов в кольцевой сети: "))
    nodes = create_ring(num_nodes)
    message = input("Введите сообщение для отправки: ")
    threading.Thread(target=nodes[0].send_message, args=(message,), daemon=True).start()
    time.sleep(5)


if __name__ == "__main__":
    main()
