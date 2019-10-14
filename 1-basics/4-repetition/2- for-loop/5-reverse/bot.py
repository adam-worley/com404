print("What phrase do you see?")
markings = input()
print()
print("Reversing...")
print()
x = len(markings)-1
print("The phrase is: ",end="")
for count in range(x, -1, -1):
    print(markings[count],end="")


    

