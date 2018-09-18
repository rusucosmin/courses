import numpy as np

class FuzzyVariable:
    def __init__(self):
        self.labels = {}
        self.value = 0

    def toDiscrete(self):
        ret = {}
        graph = self.labels
        value = self.value
        for key in graph.keys():
            #check where it is:
            for i in range(len(graph[key]) - 1):
                if graph[key][i][0] <= value and value <= graph[key][i + 1][0]:
                    if graph[key][i][0] == -np.inf:
                        ret[key] = graph[key][i][1]
                        continue
                    if graph[key][i + 1][0] == np.inf:
                        ret[key] = graph[key][i + 1][1]
                        continue
                    deltaY = graph[key][i + 1][1] - graph[key][i][1]
                    deltaX = graph[key][i + 1][0] - graph[key][i][0]
                    ret[key] = graph[key][i][1] + ((value - graph[key][i][0]) / deltaX) * deltaY
        return ret


class Texture(FuzzyVariable):
    def __init__(self, value):
        self.value = value
        self.labels = {
            'very_soft': [(-np.inf, 1), (0.2, 1), (0.4, 0), (np.inf, 0)],
            'soft': [(-np.inf, 0), (0.2, 0), (0.4, 1), (0.8, 0), (np.inf, 0)],
            'normal': [(-np.inf, 0), (0.3, 0), (0.7, 1), (0.9, 0), (np.inf, 0)],
            'resistant': [(-np.inf, 0), (0.7, 0), (0.9, 1), (np.inf, 1)]
        }


class Capactiy(FuzzyVariable):
    def __init__(self, value):
        self.value = value
        self.labels = {
            'small': [(-np.inf, 1), (1, 1), (2, 0), (np.inf, 0)],
            'medium': [(-np.inf, 0), (1, 0), (2.5, 0), (4, 0), (np.inf, 0)],
            'high': [(-np.inf, 0), (3, 0), (4, 1), (np.inf, 1)]
        }

class CycleType(FuzzyVariable):
    def __init__(self, value):
        self.value = value
        self.labels = {
            'delicate': [(-np.inf, 1), (0.2, 1), (0.4, 0), (np.inf, 0)],
            'easy': [(-np.inf, 0), (0.2, 0), (0.5, 1), (0.8, 0), (np.inf, 0)],
            'normal': [(-np.inf, 0), (0.3, 0), (0.6, 1), (0.9, 1), (np.inf, 1)],
            'intense': [(-np.inf, 0), (0.7, 0), (0.9, 1), (np.inf, 1)]
        }

class Ruler:
    def __init__(self):
        self.rules = {
            "very_soft": {
                "small": "delicate",
                "medium": "easy",
                "high": "normal"
            },
            "soft": {
                "small": "easy",
                "medium": "normal",
                "high": "normal"
            },
            "normal": {
                "small": "easy",
                "medium": "normal",
                "high": "intense"
            },
            "resistant": {
                "small": "easy",
                "medium": "normal",
                "high": "intense"
            }
        }
    def evaluate(self, t, c):
        tdic = t.toDiscrete()
        cdic = c.toDiscrete()
        resdic = {}
        print(tdic)
        print(cdic)
        for tkey, tvalue in tdic.items():
            for ckey, cvalue in cdic.items():
                res = self.rules[tkey][ckey]
                val = min(tvalue, cvalue)
                if res in resdic:
                    resdic[res] = max(resdic[res], val)
                else:
                    resdic[res] = val
        return resdic

class Controller:
    def __init__(self, texture, capacity):
        self.rules = Ruler()
        self.t = Texture(texture)
        self.c = Capactiy(capacity)

    def solve(self):
        agg = self.rules.evaluate(self.t, self.c)
        print(agg)
        print(sorted(list(agg.items()), key = lambda x: x[1])[-1][0])

c = Controller(0.4, 0.5)
c.solve()
