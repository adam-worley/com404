#find out which direction beep should paint
print("towards which direction should I paint (up, down, left or right)")
direction = input()
print()
if (direction == "up"):
    print("I am painting in the upward direction")
elif(direction == "down"):
    print("I am painting in the downward direction")
elif(direction == "left"):
    print("I am painting in the leftward direction")
elif(direction == "right"):
    print("I am painting in the rightward direction")
else:
    print("I don't know where to paint")