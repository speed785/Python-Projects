import Employee

p1 = Employee.Employee()
p2 = Employee.Employee()
p3 = Employee.Employee()

p1_Name = str(input("Please enter the Name for First employee: "))
p1_id = int(input("Please enter the Id Number for First Employee: "))
p1_Department = str(input("Please enter the Departmet of First Employee: "))
p1_Position = str(input("Please enter the Position for First employee: "))

p2_Name = str(input("Please enter the Name for Second employee: "))
p2_id = int(input("Please enter the Id Number for Second Employee: "))
p2_Department = str(input("Please enter the Departmet of Second Employee: "))
p2_Position = str(input("Please enter the Position for Second employee: "))

p3_Name = str(input("Please enter the Name for third employee: "))
p3_id = int(input("Please enter the Id Number for third Employee: "))
p3_Department = str(input("Please enter the Departmet of third Employee: "))
p3_Position = str(input("Please enter the Position for third employee: "))

def main():
    print("{0:15} {1:15} {2:15} {3:15}".format("Name","ID Number","Accounting","Position"))
    print(p1.set_Employee_info("{0:15} {1:15} {2:15} {3:15}".format(p1_Name,p1_id,p1_Department,p1_Position)))
    print(p2.set_Employee_info("{0:15} {1:15} {2:15} {3:15}".format(p2_Name,p2_id,p2_Department,p2_Position)))
    print(p3.set_Employee_info("{0:15} {1:15} {2:15} {3:15}".format(p3_Name,p3_id,p3_Department,p3_Position)))
    p1.get_Employee_info()
    p2.get_Employee_info()
    p3.get_Employee_info()
       

main()

