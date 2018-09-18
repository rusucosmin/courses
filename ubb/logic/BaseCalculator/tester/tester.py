from copy import deepcopy

__author__ = 'cosmin'

from model.integer import Integer
from random import randint
import random

#===Tester class===


class Tester:
    """
    Class used to unit-test the application

    **Tester.AllowedBases** - static array containing the allowed bases for the numbers.
    """
    AllowedBases = [2, 3, 4, 5, 6, 7, 8, 9, 10, 16]
    def __init__(self):
        pass

    def getRandomInteger(self, base):
        l = randint(1, 10)
        xrepr = ""
        for i in range(l):
            xrepr += Integer.Symbols[randint(0, base - 1)]
        x = Integer(base, xrepr)
        x.clearIsb()
        return x

    def test(self):
        for i in range(randint(1, 100)):
            self.testIntegerAddition()
        self.testConversions()
        for i in range(10):
            self.randomTestConversion()

    def randomTestConversion(self):
        x = self.getRandomInteger(10)
        y = deepcopy(x)
        for i in range(randint(1, 10)):
            newBase = random.choice(Tester.AllowedBases)
            x = x.convertToBase(newBase)
        x = x.convertToBase(10)
        assert(x == y)

    def testConversions(self):
        assert(Integer(4, "33221100").convertToBase(9) == Integer(9, "106810"))
        assert(Integer(4, "123032122").convertToBase(16) == Integer(16, "1B39A"))
        assert(Integer(4, "33221100") + Integer(4, "123032122") == Integer(4, "222313222"))
        assert(Integer(7, "1230056").convertToBase(4) == Integer(4, "212230223"))
        assert(Integer(7, "445566").convertToBase(4) == Integer(4, "103033320"))
        assert(Integer(16, "ABCDE1").convertToBase(4) == Integer(4, "222330313201"))
        assert(Integer(16, "7").convertToBase(8) ==  Integer(8, "7"))
        assert(Integer(6, "54321").convertToBase(5) == Integer(5, "214330"))
        assert(Integer(6, "3").convertToBase(2) == Integer(2, "11"))

        assert(Integer(7, "1230056") - Integer(7, "445566") == Integer(7, "451160"))
        assert(Integer(16, "ABCDE1") * Integer(16, "7") == Integer(16, "4B2A127"))
        assert(Integer(6, "54321") // 3 == Integer(6, "15304"))
        assert(Integer(6, "54321") // 4 == Integer(6, "12350"))
        assert(Integer(10, "120") % 7 == 1)
        assert(Integer(10, "17") * Integer(10, "7") + Integer(10, "1") == Integer(10, "120"))

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