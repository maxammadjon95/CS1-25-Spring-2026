class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def peek(self):
        return self.queue[0] if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0


class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        val = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val

    def peek(self):
        return self.front.data if self.front else None

    def is_empty(self):
        return self.front is None


class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else None


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            return "Full"

        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            return "Empty"

        val = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return val


if __name__ == "__main__":
    q = QueueArray()
    q.enqueue(1)
    q.enqueue(2)
    print("Dequeue:", q.dequeue())
    print("Peek:", q.peek())

    qs = QueueUsingStacks()
    qs.enqueue(10)
    qs.enqueue(20)
    print("Queue using stacks dequeue:", qs.dequeue())

    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print("Circular dequeue:", cq.dequeue())