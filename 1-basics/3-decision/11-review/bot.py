print("sup cuz it's you boy trapbot, we met in the last unit")
print ("you looking for a plug?")
plug = input()
if((plug == "yes") or (plug == "yeah")):
    print("Ok ok, what you after? snow or gelato?")
    food = input()
    if(food == "snow"):
        print("yeah yeah I can ice you out, how many packs you after?")
        snow = int(input())
        print("ok, thats £",(snow*80),"and the yute on the corner will sort you out cuz")
    elif(food == "gelato"):
        print("just got a fresh crop in, it's the real deal. how many g you after?")
        gelato = int(input())
        print("ok, thats £",(gelato*10),"and the yute on the corner will sort you out cuz")
    elif(food == "both"):
        print("ok let me know what weight your after")
        print("how many packs of white?")
        white = int(input())
        print("how many g green?")
        green = int(input())
        print("ok, thats £",((white*80)+(green*10)), "and the yute on the corner will sort you out cuz")
    else:
        print("I dont understand what your saying, stop wasting my time cuz")
elif((plug == "no")or (plug == "nah")):
    print("no worries cuzzie, catch you around yeah")
else:
    print("kmt make up your mind and get back to me my brudda")
