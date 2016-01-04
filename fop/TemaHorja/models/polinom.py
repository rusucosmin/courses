from copy import deepcopy


class Polinom:
    '''
    Clasa care incapsuleaza un polinom
        self.grad = gradul polinomului
        self.coef = coeficientii polinomului

        P = self.coef[0] + self.coef[1] * X + ... + self.coef[i] * X ^ i + ...

    Polinom
        Specificaţi şi implementaţi tipurile abstracte de date menţionate mai jos.
        La toate tipurile de date vor exista operaţii pentru:

        a) creare de valori din domeniul tipului respectiv;
        b) operaţii aritmetice
        c) comparare de valori
        d) extragere de componente
        e) eventual conversii din alte tipuri mentionate.

    '''
    def __init__(self, grad, coef):
        self.grad = grad
        self.coef = coef

    def getCoef(self):
        return self.coef

    def len(self):
        return self.grad

    def __getitem__(self, item):
        return self.coef[item]

    def __setitem__(self, key, value):
        self.coef[key] = value

    def add(self, other):
        new_grad = max(self.grad, other.grad)
        new = Polinom(new_grad, [0] * new_grad)
        for i in len(self):
            new[i] = new[i] + self[i]
        for i in len(other):
            new[i] = new[i] + other[i]
        new.clearLeadingZero()
        return new

    def clearLeadingZero(self):
        while len(self) and self[-1] == 0:
            self.grad -= 1
            self.coef = self.coef[:-1]

    def sub(self, other):
        new_grad = max(self.grad, other.grad)
        new = Polinom(new_grad, [0] * new_grad)
        for i in len(self):
            new[i] = new[i] + self[i]
        for i in len(other):
            new[i] = new[i] - other[i]
        new.clearLeadingZero()
        return new

    def value(self, x):
        ans = 0
        for i in self.coef[::-1]:
            ans = ans * x + i
        return ans

    def cmp_value(self, other, x):
        if self.value(x) > other.value(x):
            return -1
        elif self.value(x) == other.value(x):
            return 0
        else:
            return 1