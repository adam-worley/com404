print("what level of brightness is required")
n = int(input())
x=0
print()
print("adjusting brightness...")
print()
if (n%2 ==0):
    for count in range (0, n, 2):
        x = x+2
        print("Beep's brightness level:",x*"*")
        print("Bop's brightness level:",x*"*")
        print()
else:
    while (n%2 !=0):
        print("please enter an even value")
        n = int(input())
        print()
    for count in range (0, n, 2):
        x = x+2
        print("Beep's brightness level:",x*"*")
        print("Bop's brightness level:",x*"*")
        print()
print()
print("adjustments complete!")