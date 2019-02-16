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
Celsius=eval(input("Please Enter a temperature in Celsius you would like to convert: "))
Fahrenheit=eval(input("Please Enter a temperature in Farenheit you would like to convert: "))



# Math #
# (F - 32) * 5/9 = C #
# (C * 9/5) + 32 = F #

# What is shown #
#print("Fahrenheit Conversion = ", Fahrenheit)
#print("Celsius Conversion = ", Celsius)

#####
#Extra testing using the for loop


print("{0:10} {1:20} {2:20} {3:20}".format("Celsius", "Farenheit", "Values for F to C", "Values for C to F",))
i=0
for i in range(15):
    # variables #
    cel=round(((Fahrenheit - 32) * 5/9), 2)
    far=round(((Celsius * 9/5) + 32), 2)
    print("{0:<10.2f} {1:10.2f} {2:20.2f} {3:20.2f}".format(cel, far, Celsius, Fahrenheit))
    Fahrenheit += 1
    Celsius += 1
    
    

