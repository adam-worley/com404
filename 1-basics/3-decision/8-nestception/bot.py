print("where should I look")
location_1 = input()
if(location_1 == "in the bedroom"):
    print("where in the bedroom should I look")
    room_location_1 = input()
    if(room_location_1 == "under the bed"):
        print("found some shoes but no battery")
    else:
        print("I found some mess but no battery ")
elif(location_1 == "in the bathroom"):
    print("where in the bathroom should I look")
    room_location_1 = input()
    if(room_location_1 == "in the bath"):
        print("found a rubber duck but no battery")
    else:
        print("it is wet but I found no battery ")
elif(location_1 == "in the lab"):
    print("where in the lab should I look")
    room_location_1 = input()
    if(room_location_1 == "on the table"):
        print("yes! i found my battery")
    else:
        print("found some tools but no battery")
else:
    print("I don't know where that is but I will keep looking")