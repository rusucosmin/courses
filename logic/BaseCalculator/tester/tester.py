__author__ = 'cosmin'

from model.integer import Integer
from random import randint
import random

class Tester:
    AllowedBases = [2, 3, 4, 5, 6, 7, 8, 9, 10, 16]
    def __init__(self):
        pass

    def getRandomInteger(self, base):
        l = randint(1, 10)
        xrepr = ""
        for i in range(l):
            xrepr += Integer.Symbols[randint(0, base - 1)]
        x = Integer(base, xrepr)
        return x

    def test(self):
        for i in range(randint(1, 100)):
            self.testIntegerAddition()

    def testIntegerAddition(self):
        base = random.choice(Tester.AllowedBases)
        x = self.getRandomInteger(base)
        y = self.getRandomInteger(base)
        z = x + y
        assert(self.convertToBase10(repr(x), base) + self.convertToBase10(repr(y), base) == self.convertToBase10(repr(z), base))

    def convertToBase10(self, number, base):
        x = 0
        for i in range(len(number)):
            x = x * base + Integer.Values[number[i]]
        return x