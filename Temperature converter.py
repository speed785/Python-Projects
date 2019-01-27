#Coded by : James Dumitru

# input #
y=int(input("Please Enter A Number "))
x=int(input("Please Enter A Second Number "))

# variables #
add=x+y
multi=x*y
div=x/y
sub=x-y
mod=x%y

# What is shown #
print("This is the addition for the two numbers=", add)

print("This is the multiplication for the two numbers=", multi)

print("This is the division for the two numbers=", div)

print("This is the subtraction for the two numbers=", sub)

print("This is the mod for the two numbers=", mod)

# input for Temperature Conversion #
Celsius=int(input("Please Enter a temperature in Celsius you would like to convert"))
Fahrenheit=int(input("Please Enter a temperature in Farenheit you would like to convert"))

# variables #
Celsius=round(((Fahrenheit - 32) * 5/9), 3)
Fahrenheit=round(((Celsius * 9/5) + 32), 3)

# Math #
# (F - 32) * 5/9 = C #
# (C * 9/5) + 32 = F #

# What is shown #
print("Fahrenheit Conversion = ", Fahrenheit)
print("Celsius Conversion = ", Celsius)
