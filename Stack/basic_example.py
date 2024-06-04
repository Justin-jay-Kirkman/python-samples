class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            self.length -= 1
            return value
        else:
            raise IndexError('Stack is empty and thus you cannot pop')

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.length += 1
    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise IndexError('Stack is empty and thus you cannot peek')

    def size(self):
        return self.length


stack = Stack()
array = [1,2,3,4,5,6,7,8,9]
for i in array:
    stack.push(i)

print(stack.peek())
print(stack.size())

for i in range(len(array)):
    stack.pop()
print(stack.peek())
print(stack.size())

# Linked list example
# list = []
# for i in array:
#     list.append(i)
#
# print(list[len(array)-1])
# print(len(list))
#
# for i in range(len(array)):
#     list.pop()
# if len(array) <= 0:
#     print(list[len(array)-1])
# else:
#     print("None")
# print(len(list))
