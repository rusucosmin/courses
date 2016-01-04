class Timp:
    '''
    Specificaţi şi implementaţi tipurile abstracte de date menţionate mai jos.
        La toate tipurile de date vor exista operaţii pentru:

        a) creare de valori din domeniul tipului respectiv;
        b) operaţii aritmetice
        c) comparare de valori
        d) extragere de componente
        e) eventual conversii din alte tipuri mentionate.
    '''
    def __init__(self, ora = 0, minute = 0, secunde = 0):
        self.ora = ora
        self.minute = minute
        self.secunde = secunde

    def __repr__(self):
        return '{:02d}:{:02d}:{:02d}'.format(self.ora, self.minute, self.secunde)

    def __str__(self):
        return repr(self)


    def setOra(self, ora):
        self.ora = ora

    def setMinute(self, minute):
        self.minute = minute

    def setSecunde(self, secunde):
        self.secunde = secunde

    def getOra(self):
        return self.ora

    def getMinute(self):
        return self.minute

    def getSecunde(self):
        return self.secunde

    def tickSecunda(self):
        self.secunde += 1
        if self.secunde >= 60:
            self.secunde = 0
            self.tickMinute()

    def tickMinute(self):
        self.minute += 1
        if self.minute >= 60:
            self.minute = 0
            self.tickOra()

    def tickOra(self):
        self.ora += 1
        if self.ora >= 24:
            self.ora = 0

    def __add__(self, other):
        tmp = Timp(0, 0, 0)
        tmp.secunde = self.secunde + other.secunde
        tmp.minute = self.minute + other.minute + (tmp.secunde // 60)
        tmp.secunde %= 60
        tmp.ora = self.ora + other.ora + (tmp.minute // 60)
        tmp.minute %= 60
        tmp.ora %= 24
        return tmp

    def compare(self, other):
        if self.ora > other.ora:
            return -1
        elif self.ora < other.ora:
            return 1
        elif self.minute > other.minute:
            return -1
        elif self.minute < other.minute:
            return 1
        elif self.secunde > other.secunde:
            return -1
        else:
            return 0

    def __gt__(self, other):
        return self.compare(other) == -1

    def __lt__(self, other):
        return self.compare(other) == 1

    def __eq__(self, other):
        return self.compare(other) == 0

    def __le__(self, other):
        return self.compare(other) >= 0

    def __gt__(self, other):
        return self.compare(other) <= 0