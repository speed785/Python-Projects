def main():
    ## Demonstrate the scope of local variables.
    global x
    x = 5
    trivial()

def trivial():
    print(x)

main()