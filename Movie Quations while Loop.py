## Movie Quotations
print("This program displays a famous movie quotation.")
responces = ('1','2','3')
responce = '0'
while responce not in responces:
    responce = input("Enter 1,2, or, 3: ")
    if responce == '1':
        print("Plastics.")
    elif responce == '2':
        print("Rosebud.")
    elif responce == '3':
        print("That's all folks.")
