"""Write a program to check if two strings are a 
rotation of each other?"""

def rotational_string(s1, s2):
    if len(s1) != len(s2):
        return False
    
    temp = s1 + s1

    if s2 in temp:
        return True
    return False

string1 = input("Enter 1st string: ")
string2 = input("Enter 2nd string: ")
if rotational_string(string1, string2):
    print("Given Strings are rotations of each other.")
else: 
    print("Given Strings are not rotations of each other.")