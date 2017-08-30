# For loop with a count
import time


##i = 0
##for i in range(3):
##
##    print("this is loop %s " %i)
##    time.sleep(.5)
##    
##    
##print()

# While loop with test
u = 1
i = 4
grade = 0

while grade != 1:
    grade = int(input("Type A Number Here----> "))
    if grade < 10:
        print("potato")
    elif grade < 200:
        print("your shoe is untied")
    elif grade < 300:
        print("you win a taco")
    elif grade < 400:
        print("your shoe is watermelon, watermelon, watermelon")
    elif grade < 500:
        print("you've won ONE MILLION ROBUX!!!!!!")
    elif grade < 6000:
        print("you are a duck")      
    else:
        print("you win everything, your computer is sad")
    print ("Input a number, please, to play our game.")
    
    #60print("this is loop %s " %i)
    i=i-1


# Nested loop
for i in range(3): 
    for j in range(4):
        print(" This is outside",i,"this is inside", j)
        time.sleep(2)
    time.sleep(.3)

