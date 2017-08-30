# Import modules
import time

# Create a list for spells

wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']


print("the whole list")
print(wizard_list)

print("--------------------")

print("each item")
print(wizard_list[0])
print(wizard_list[1])
print(wizard_list[3])
print(wizard_list[2])

input('Press Enter')
print("--------------------")

for i in wizard_list: 
    print(" This is item", i)
    time.sleep(.3)


input('Press Enter')
print("--------------------")
s = int(input('Item 1-6: '))
print(wizard_list[s-1])

input('Press Enter')
print("--------------------")


print(wizard_list[2:5])

wizard_list.append('bear burp')
print(wizard_list)
print("--------------------")
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)
input('Press Enter')
print("--------------------")
del wizard_list[5]
print(wizard_list)
del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
print(wizard_list)
