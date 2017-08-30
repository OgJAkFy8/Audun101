def Add6(numA):
    NumAdd6 = numA + 6
    return NumAdd6

def Add4(numA):
    NumAdd4 = numA + 4
    return NumAdd4

def Add3(numA):
    NumAdd3 = numA + 3
    return NumAdd3

def Add8(numA):
    NumAdd8 = numA + 8
    return NumAdd8

def DiceRoll(d_side,rolls):
    import random
    while rolls != 0:
        roll = random.randint(1,d_side)
        print("Roll -",roll)
        rolls=rolls-1
    
        


    
