#Tower Of Hanoi

def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print("Move Disk 1 From", source, "To", destination)
        return
    tower_of_hanoi(n - 1, source, destination, helper)
    print("Move Disk", n, "From", source, "To", destination)
    tower_of_hanoi(n - 1, helper, source, destination)

#Number Of Disks
n = int(input("Enter Number of Disks: "))

#Solve Tower Of Hanoi
tower_of_hanoi(n, "A", "B", "C")

#Total Number Of Moves
print("Total Moves: ", (2 ** n) - 1)
