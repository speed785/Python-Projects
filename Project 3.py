menu = {}
menu['1']="Filled Triangle." 
menu['2']="Filled Square."
menu['3']="Filled Circle."
menu['4']="Bow Tie Shape."
menu['5']="Exit."


while True: 
  options=menu.keys()
  options.sort()
for entry in options: 
        print (entry, menu[entry])
    selection=raw_input("Please Select:") 
    if selection =='1': 
        print "Triangle."
        numberOfRows = int(50) 
for i in range (numberOfRows):
for j in range(i + 1):
        print("*", end="")
    print()
    elif selection == '2': 
        print "Square"
    elif selection == '3':
        print "Circle" 
    elif selection == '4':
        print "Bow Tie"   
    elif selection == '5': 
        break
    else: 
        print "Unknown Option Selected!" 