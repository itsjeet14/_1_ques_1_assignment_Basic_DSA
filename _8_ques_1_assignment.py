"""Write a program to reverse a stack."""
def reverse_stack(stack):
    if not stack:
        return
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)

def insert_at_bottom(stack, value):
    if not stack:
        stack.append(value)
        return
    temp = stack.pop()
    insert_at_bottom(stack, value)
    stack.append(temp)

len_stack = int(input("Enter lenght of stack: "))
stack = []
for i in range(len_stack):
    element = int(input("Enter element is stack: "))
    stack.append(element)


print("Original stack:", stack)
reverse_stack(stack)
print("Reversed stack:", stack)
