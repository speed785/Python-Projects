while True:
    try:
        numDependants = int(input("Enter number of dependants: "))
        numDependants = 0
        taxCredit = 1000 * numDependants
        print("Tax credit:", taxCredit)
        print("\nYou did not respond with an integer value.")
        print("We will assume your answer is zero. \n")
    except ValueError: 