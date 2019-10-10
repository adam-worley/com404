print("How many bars should be charged?")
bars = int(input())
charge = 0
print()
while(bars > charge):
    charge = charge+1
    print("charging:",charge*"█ ")
    if charge == 5:
        break
print()
if charge == 5:
    print("The battery is fully charged.")
else:
    print("The battery is not fully charged.")
