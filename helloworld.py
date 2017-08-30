# Print something to the shell
print('hello world')

# Set a variable
numA = 3
numB = 8

# Add the two variables
numADD = numA + numB

#Print the variable
print(numADD)

# Do more math with numA and numB
numMult = numA * numB
print('A * B =',numMult)

# ---------------------------------

numDiv = numB / numA
print('B / A =',numDiv)

numMod = numB - numA
print('B / A =',numMod)



# ====================
# IF Statements

ifA = str('3')
ifB = str('red')


int(ifA)

if ifA != ifB:
    print("These are NOT equal: " + ifA + " and " + ifB)
else:
          print("done")

print()



#-----------------------------------
import AddNums
from GameMath2 import diceroll, coinflip
# from GameMath import coinflip

print("Calling Modules")

t = AddNums.Add6(6)
diceroll(6,5)
coinflip(1)

coinflip(9,"T")
