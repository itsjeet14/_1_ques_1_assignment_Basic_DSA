""" Write a program to find the smallest number using a stack."""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def find_smallest(stack):
    if stack.is_empty():
        return None
    smallest = stack.pop()
    if not stack.is_empty():
        temp = find_smallest(stack)
        if temp < smallest:
            smallest = temp
    stack.push(smallest)
    return smallest

stack = Stack()
stack.push(4)
stack.push(8)
stack.push(1)
stack.push(5)
stack.push(2)
print("Stack:", stack.items)
smallest = find_smallest(stack)
print("Smallest number in stack:", smallest)
