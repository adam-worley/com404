def cross_bridge (steps):
    x = 0
    while (steps>0):
        print("Crossed step")
        steps = (steps-1)
        x = x+1
    if (x>=5):
        print("The bridge is collapsing!")
    else:
        print("we must keep going")
    

cross_bridge(3)
cross_bridge(6)
