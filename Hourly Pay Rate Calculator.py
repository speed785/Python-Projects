#Coded by : James Dumitru

# input #
Name = input("Please Enter You're First and Last Name: ")
Hours = float(input("Please Enter You're Hours Worked For This Week: "))
Hourlypayrate = float(12.50)

# calculations for weekly, bi-weekly, monthly, yearly pay#
weekly = (Hours * Hourlypayrate)
biweekly = (weekly*2)
monthly = (biweekly*2)
yearly = (monthly*12)

# reveal the weekly, bi-weekly, monthly, and yearly pay in that order#
print(Name ,", given your hours worked:")

print(("You're weekly pay is: ", weekly))

print(("You're biweekly pay is: ", biweekly))

print(("You're monthly pay is: ", monthly))

print(("You're yearly pay is: ", yearly)) 