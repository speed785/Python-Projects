import emp


def main():

    databse = {} #create dictionary

    for i in range(3):
        name = input("Please enter the Name for First employee: ")
        id = input("Please enter the Id Number for First Employee: ")
        department = input("Please enter the Departmet of First Employee: ")
        position = input("Please enter the Position for First employee: ")
        e=emp.Employee(name, id, department,position) #create object for dictionary
        databse[i]=e #adds e into database


    for i in range(3):
        print(databse.get(i, "invalid")) #if 'i' isn't found it returns it as invalid

main()
