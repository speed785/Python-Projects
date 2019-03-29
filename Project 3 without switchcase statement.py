# Coded by James Dumitru
import math

# Triangle if chosen number 1
def Triangle(size):
  for l in range (size):
      for w in range(l + 1):
          print(".", end="")
      print()

# Square if chosen number 1  
def Square(size):
    for box in range(size):
      print (' . ' * size)
    print()

# Rectangle if chosen number 1  
def Rect(size):
    for height in range(int(size/2)):
        for width in range(size):
            print(".",end=" ")
        print()

# Attempt at bowtie    
# BowTie if chosen number 1
def BowTie(size):
    for b in range(size+1):
        for angle in range(size):
            if angle <=(size/2):
                if b>=angle or angle>=(size-b-1):
                    print("*",end="")
                else:
                    print("",end=".")
            else:
                if angle<=(size-b) or angle>=(b-1):
                    print("*",end="")
                else:
                    print("",end=".")
        print()
        
# Menu with 1-5 options.
# If pressed 1-4, it will give a shape.
# If pressed 5, the program will end.  
if __name__ == '__main__':
    while True:
        print("Please pick an below: ")
        print("1. Filled Triangle")
        print("2. Filled Square")
        print("3. Filled Rectangle")
        print("4. Bow Tie shape")
        print("5. Exit")
        choice = int(input("Enter your choice from 1-5: "))
        if(choice==5) : break
        else:
            size = int(input("Enter the size from 1-50: "))
            if (choice==1) : Triangle(size)
            if (choice==2) : Square(size)
            if (choice==3) : Rect(size)
            if (choice==4) : BowTie(size)  
        print("\n")