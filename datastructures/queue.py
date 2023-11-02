class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Die Queue ist leer.")

    def size(self):
        return len(self.items)

# Beispielverwendung der Queue
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue-Größe:", queue.size())

print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())

print("Queue-Größe nach Dequeue:", queue.size())
print("Dequeue:", queue.dequeue())
print("Queue-Größe nach Dequeue:", queue.size())