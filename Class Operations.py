#Coded by : James Dumitru

class Operations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    #Mutator methods
    def addtion(self, num1, num2):
        result = num1 + num2 
        return result
    def subtraction(self, num1, num2):
        result = num1 - num2
        return result
    def multiplication(self, num1, num2):
        result = num1 * num2
        return result
    def division(self, num1, num2):
        result = num1 // num2
        return result


