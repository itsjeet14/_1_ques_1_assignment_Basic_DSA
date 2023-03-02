"""Read about the Tower of Hanoi algorithm. 
Write a program to implement it."""
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, source, destination)

n = int(input("Enter the number of disks to move: "))
source = input("Enter the rod from which to move the disks: ")
auxiliary = input("Enter the auxiliary rod to use in the moves: ")
destination = input("Enter the rod to which to move the disks: ")
tower_of_hanoi(n, source, auxiliary, destination)
