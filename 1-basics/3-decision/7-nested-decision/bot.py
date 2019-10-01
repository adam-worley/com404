print("what type of cover does the book have?")
cover = input()
print()
if(cover =="soft"):
    print("is the book perfect bound?")
    bound = input()
    print()
    if(bound == "yes"):
        print("soft cover, perfect bound books are very popular!")
    else:
        print("soft covers with coils or stitches are great for short books")
elif(cover == "hard"):
    print("books with hard covers can be more expensive")
else:
    print("i don't know what book this is")
