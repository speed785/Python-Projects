## Determine the larger of the two numbers.
# Obtain the two numbers from the user.
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
# Determine the display and the lerger value.
if num1 > num2:
    largerValue = num1  # execute this statement if the condition is true
else: 
    largerValue = num2  # execute this statement if the condition is false
print("The larger value is", str(largerValue) + ".")
