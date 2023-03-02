""" Write a program to print the first non-repeated 
character from a string?"""

def non_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    return None

string = input("Enter string: ")
result = non_repeated_char(string)

if result:
    print(f"The first non-repeated character in '{string}' is '{result}")
else:
    print(f"There is no non-repeated character in '{string}")




