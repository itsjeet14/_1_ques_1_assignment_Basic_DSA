"""Write a program to check if all the brackets are 
closed in a given code snippet."""
def is_balanced(code):
    stack = []
    for char in code:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False
    return not stack

code = input("Enter code snippet: ")
if is_balanced(code):
    print("All brackets are closed.")
else:
    print("Brackets are not balanced.")
