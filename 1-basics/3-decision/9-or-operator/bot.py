print("what type of adventure should I have")
adventure = input()
print()
if((adventure == "scary") or (adventure == "short")):
    print("entering the dark forest!")
elif((adventure == "safe") or (adventure == "long")):
    print("taking the safe route!")
else:
    print("not sure which route to take")
