class LGstudent(Student):
    def calcSemgrade(self):
        average = round((self.__midterm + self.__final) / 2)
        if average >= 60:
        return "Pass"
    else:
        return "Fail"