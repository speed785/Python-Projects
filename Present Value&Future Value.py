def main(cash):
    print(round(cash,2))
def shmoney():
    start = int(eval(input("Enter the amount you wish to begin: ")))
    #Future value
    F = int(eval(input("Enter the amount you wish to have: ")))
    #annual interest rate
    r = int(eval(input("Enter the rate: ")))
    #number of years
    n = int(eval(input("Enter the time in years you have to save: ")))
    #Present Value Equation
    global cash
    cash = F/((1+r)**n)+start
    return cash
shmoney()      
main(cash)
