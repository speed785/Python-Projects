#Coded by James
#This python code will run a coin toss to how many times you want it to flip.

import Cointoss

o=Cointoss.Coin() 
print("_________________________")
print("The side of the coin is:")
print("_________________________")
print(o.getSideUp())

for x in range(0,20):
    o.toss()
    print(o.getSideUp())
print("_________________________")
print("\nThe number of heads is: ")
print(o.getNumHeads())
print("_________________________")
print("\nThe number of tails is: ")
print(o.getNumTails())
