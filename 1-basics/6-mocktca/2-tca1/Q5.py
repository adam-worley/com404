#set variable for health
health=100
#set a constant to repeat loop
repeat=5
#Start code for programme. +str(health+ is used to remove the space between the value and % to match questions output.
print("Your health is "+str(health)+"%. Escape is in progress ...")
#Start loop
while(repeat>0):
    print("...Oh dear, who is that?")
    robot=str(input())
    if(robot =="Smiler's Bot"):
        health=health-20
        print("Time to jam out off here!")
    elif(robot=="Hacker"):
        health=health+20
        print("Yay! Better follow this one!")
    else:
        print("Phew, just another emoji!")
        health=health
    repeat=repeat-1
    print()
#Recall health
print("Escaped! Health is "+str(health)+"%.")