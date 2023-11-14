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

enqueue_value = 1
print("Enqueue:", enqueue_value)
queue.enqueue(enqueue_value)
enqueue_value = 2
print("Enqueue:", enqueue_value)
queue.enqueue(enqueue_value)
enqueue_value = 3
print("Enqueue:", enqueue_value)
queue.enqueue(enqueue_value)

print("Queue-Größe nach Enqueue:", queue.size())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Queue-Größe nach Dequeue:", queue.size())
print("Dequeue:", queue.dequeue())
print("Queue-Größe nach Dequeue:", queue.size())