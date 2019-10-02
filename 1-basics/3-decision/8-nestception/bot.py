print("where should I look")
location_1 = input()
if(location_1 == "bedroom"):
    print("where in the bedroom should I look")
    room_location_1 = input()
    if(room_location_1 == "in the cupboard"):
        print("found some mess but no battery")
        print()
        print("where should I look")
        location_2 = input()
        if(location_2 == "bedroom"):
            print("I have already looked here, where should i look?")
            location_2 = input()
    else:
        print("I can't look there, where in the bedroom should I look?")
       
        


