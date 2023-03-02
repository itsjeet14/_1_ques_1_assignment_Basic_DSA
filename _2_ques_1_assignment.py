"""Q2. Write a program to reverse an array in place? 
In place means you cannot create a new array. 
You have to update the original array."""

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    if left < right:
        arr[left], arr[right] = arr[right], arr[left]
        
        left += 1
        right -= 1

len_array = int(input("Enter length of array: "))
array = []
for i in range(len_array):
    elment = int(input("Enter element: "))
    array.append(elment)

print("Array: ", array)
reverse_array(array)
print("Reverse Array: ", array)
    