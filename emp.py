##James Dumitru

#create a class named Employee
class Employee:

    #initialize the attributes
    def __init__(self, name, id, department, title):
        self.__name = name
        self.__id = id
        self.__department = department 
        self.__title = title

 

    #return the objects state as a string

    def __str__(self):
        return '\nName: ' + self.__name + \
        '\nID number: ' + self.__id + \
        '\nDepartment: ' + self.__department + \
        '\nTitle: ' + self.__title

