print("How many rows should I have?")
row = int(input())
print()
print("How many columns should I have?")
column = int(input())
print()
print("Here I go:")
print()
for count in range (0, row, 1):
    for number in range (0,column,1):
        print(":-)", end=" ")
    print()
print()
print("Done!")