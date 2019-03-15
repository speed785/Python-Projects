def main():
    global a1
    global a2
    a1=eval(input("Please enter your first number."))
    a2=eval(input("Please enter your second number."))
    addition (a1, a2)
    multiplication(a1, a2)
    subtraction (a1, a2)
    division (a1, a2)

def addition(a1,a2):
    add = a1 + a2
    print("The addition between the two numbers is: ", add)
    return add

def multiplication(a1,a2):
    mult = a1 * a2
    print("The multiplication between the two numbers is: ", mult)
    return mult

def subtraction(a1,a2):
    sub = a1 - a2
    print("The subtraction between the two numbers is: ", sub)
    return sub

def division(a1,a2):
    div = a1 / a2
    print("The division between the two numbers is", div)
    return div

main()