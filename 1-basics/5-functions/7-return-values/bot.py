def sum_weights (bop_weight,beep_weight):
    weight = (bop_weight + beep_weight)
    print("The sum of Beep and Bop's weight is",weight)

def calc_avg_weight (bop_weight,beep_weight):
    avg_weight = (bop_weight+beep_weight)/2
    print("The average of Beep and Bop's weight is",avg_weight)

def run ():
    print("What is the weight of beep")
    bop_weight= float(input())
    print()
    print("What is the weight of bop")
    beep_weight = float(input())
    print()
    print("what would you like to calculate (sum or average)?")
    calculate = input()
    print()
    if (calculate == "sum"):
        sum_weights(bop_weight,beep_weight)
    elif (calculate == "average"):
        calc_avg_weight(bop_weight,beep_weight)
    else:
        print("I don't know that calculation")

run()