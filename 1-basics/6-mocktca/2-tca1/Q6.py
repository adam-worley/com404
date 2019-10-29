def is_league_united(hero_1,hero_2):
    if(hero_1=="Superman" or hero_1=="Wonder Woman"):
        if(hero_2=="Superman" or hero_2=="Wonder Woman"):
            result=True
        else:
           result=False
    else:
        result=False
    return result

def decide_plan(hero_1,hero_2):
    is_league_united(hero_1,hero_2)
    if(result==True):
        print("Time to save the world!")
    elif(result==False):
        print("We must unite the league!")

def run():
    print("Enter the first hero name")
    hero_1=input()
    print("Enter the second hero name")
    hero_2=input()
    print("What function do you require?")
    function=input()
    if(function=="league"):
       result = is_league_united(hero_1,hero_2)
    elif(function=="plan"):
        decide_plan(hero_1,hero_2)
    else:
        print("Invalid command. Please try again")

run()


