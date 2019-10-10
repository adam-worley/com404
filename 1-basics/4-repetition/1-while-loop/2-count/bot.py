print("How many live cables should I avoid?")
cable = int(input())
n = 0
print()
while(cable >0):
    cable = cable-1
    n = n + 1
    print("avoiding...Done!", n,"live cable avoided.")
print()
print("All live cables have been avoided")