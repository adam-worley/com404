print ("how many steps are we away from the cave?")
n = int(input())
print()
for count in range(n, 0, -1):
    n = n-1
    print(n, "steps remaining")
print()
print("we have reached the cave!")