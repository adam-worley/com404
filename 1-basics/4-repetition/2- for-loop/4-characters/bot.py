print("what strange markings do you see?")
markings = input()
print()
print("identifying...")
print()
x = 0
for position in range(0, len(markings),1):
    print("index",x,":", markings[position])
    x = x+1
print()
print("done!")
