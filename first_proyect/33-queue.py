class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        return self.items.pop(0) if not self.is_empty() else None

    def peek(self):

        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.size())