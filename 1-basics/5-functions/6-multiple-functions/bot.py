def display_ladder (steps):
    while(steps>0):
        print("| |")
        print("***")
        steps = (steps-1)

def create_ladder():
    print("How many steps remain?")
    x = int(input())
    print()
    display_ladder(x)

create_ladder()