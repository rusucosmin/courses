from model.integer import Integer
from exception.integerexception import IntegerException

class Calculator:
    Menu = [1, 2, 3, 4, 5]
    def __init__(self, controller):
        self._controller = controller

    def printMainMenu(self):
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division with one digit")
        print("5. conversion")

    def getInteger(self):
        base = int(input("Insert base: "))
        s = input("Insert number representation: ")
        return Integer(base, s)

    def getOperands(self):
        x = self.getInteger()
        y = self.getInteger()
        return x, y

    def run(self):
        while True:
            try:
                self.printMainMenu()
                op = int(input("Please input the type of operation you want to do: "))
                if op == 1:
                    x, y = self.getOperands()
                    print(self._controller.add(x, y))
                elif op == 2:
                    x, y = self.getOperands()
                    print(self._controller.sub(x, y))
                elif op == 3:
                    x, y = self.getOperands()
                    print(self._controller.mul(x, y))
                elif op == 4:
                    x = self.getInteger()
                    y = self.getOneDigitInteger()
                    print("quotient: ", self._controller.div(x, y))
                    print("remainder: ", self._controller.mod(x, y))
            except ValueError:
                print("Value should be integer.")
            except IntegerException as ie:
                print(ie)