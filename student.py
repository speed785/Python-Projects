print(st)
class LGstudent:
    def __init__(self, name="", midterm=0, final=0):
        self.__name = nameself.midterm = midterm
        self.__midterm = midterm
        self.final = final 
class Student:
    def __init__(self, name="", midterm=0, final=0):
        self.__name = nameself.midterm = midterm
        self.__midterm = midterm
        self.final = final 
    def setName(self, name):
            self.__name = name
    def setMidterm(self, midterm):
        self._midterm = midterm
    def setFinal(self, final):
        self.__final = final
    def getName(self):
        return self.__name
    def __str__(str):
        return self.__name + "\t" + self.calcSemGrade()
class LGstudent(Student):
    def calcSemgrade(self):
        average = round((self.__midterm + self.__final)/2)
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C' 
    elif average >= 60:
        return 'D'
    else:
        return: 'F'
class PFstudent(Student):
    def calcSemgrade(self):
        average = round((self.__midterm + self.__final) / 2)
    if average >= 60:
        return "Pass"
    else:
        return "Fail"
