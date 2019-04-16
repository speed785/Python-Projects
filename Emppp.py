class Employee():
    def _init_ (self, Name, idNumber, department, position):
        self.Name = Name
        self.idNumber = idNumber
        self.department = department
        self.position = position

    def set_Employee_info(self, Name, id, department, position):
        self.Name = Name
        self.idNumber = id
        self.department = department
        self.position = position

    def get_Employee_info(self): 
        print(self.Name , self.idNumber, self.department,self.position )
