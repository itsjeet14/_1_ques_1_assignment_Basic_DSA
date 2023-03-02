"""Write a program to convert prefix expression to 
infix expression."""

def prefix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for char in reversed(expression):
        if char in operators:
            left_operand = stack.pop()
            right_operand = stack.pop()

            infix = f"({left_operand}{char}{right_operand})"
            stack.append(infix)
        else:
            stack.append(char)
    return stack.pop()

prefix_expression = input("Enter the expression: ")
infix_expression = prefix_to_infix(prefix_expression)
print(f"The infix expression of '{prefix_expression}' is '{infix_expression}'")