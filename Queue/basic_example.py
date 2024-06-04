class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, value): #adds to the rear
        node = Node(value)
        self.length += 1
        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self): # removes from the front
        if not self.front:
            raise IndexError('Queue is empty')
        value = self.front.value
        self.front = self.front.next
        self.length -= 1
        return value


q = Queue()
array = [1,2,3,4,5,6,7,8,9]

for i in array:
    q.enqueue(i)

for i in range(q.length):
    print(q.dequeue())