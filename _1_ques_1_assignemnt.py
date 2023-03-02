"""Q1. Write a program to find all pairs of an 
integer array whose sum is equal to a given number?"""

def find_pairs(arr, sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                pairs.append((arr[i],arr[j]))
    return pairs

arr = []
sum = int(input("Enter the sum: "))
len_arr = int(input("Enter length of array: "))

for k in range(len_arr):
    element = int(input("Enter array elment: "))
    arr.append(element)

print("Array: ",arr)

print("Pairs of sum %d :"%sum,find_pairs(arr, sum))
