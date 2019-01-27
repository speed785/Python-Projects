#Coded by : James Dumitru

# input #
Name=input("Please Enter You're First and Last Name: ")
Hours=int(input("Please Enter You're Hours Worked For This Week: "))

Hourlypayrate=12.50

# needs to display weekly, bi-weekly, monthly, yearly #

weekly=round(Hours*Hourlypayrate, 3)
biweekly=round(weekly*2, 3)
monthly=round(biweekly*2, )
yearly=round(monthly*12, 3)

# reveal the weekly,bi-weekly,monthly, and yearly pay in that order#

print(Name ,":")

print("You're weekly pay is: ", weekly)

print("You're biweekly pay is: ", biweekly)

print("You're monthly pay is: ", monthly)

print("You're yearly pay is: ", yearly)