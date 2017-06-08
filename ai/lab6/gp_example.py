'''
Some specific functions for a GP variation
'''

from random import randint,random

DEPTH_MAX=5
terminals=['U','RS','V','c1','c2','c3','c4','c5']
noTerminals=8
functions=['+','-','*']
noFunctions=3

class Chromosome:
    def __init__(self, d=DEPTH_MAX):
        self.mDepth=d
        self.repres=[0 for i in range(2**(self.mDepth+1)-1)]
        self.fitness=0
        self.size=0

    def growExpression(self, pos=0, depth=0):
        """
        initialise randomly an expression
        """
        if (pos==0)or(depth<self.mDepth):
            if random()<0.5:
                self.repres[pos] = randint(1, noTerminals)
                self.size=pos+1
                return pos + 1
            else:
                self.repres[pos] = -randint(1,noFunctions)
                finalFirstChild =self.growExpression(pos+1, depth+1)
                finalSecondChild = self.growExpression(finalFirstChild, depth+1)
                return finalSecondChild
        else:
                #choose a terminal
            self.repres[pos] = randint(1, noTerminals)
            self.size=pos+1
            return pos + 1

    def evalExpression(self, pos, crtData):
        """
        the expresion value for some specific terminals
        """
        if  self.repres[pos]>0: # a terminal
            return crtData[self.repres[pos]-1], pos    
        elif self.repres[pos]<0:  #a function
            if functions[-self.repres[pos]-1]=='+':
                auxFirst=self.evalExpression(pos+1,crtData)
                auxSecond=self.evalExpression(auxFirst[1]+1,crtData)
                return auxFirst[0]+auxSecond[0],auxSecond[1]
            elif functions[-1-self.repres[pos]]=='-':
                auxFirst=self.evalExpression(pos+1,crtData)
                auxSecond=self.evalExpression(auxFirst[1]+1,crtData)
                return auxFirst[0]-auxSecond[0],auxSecond[1]
            elif functions[-1-self.repres[pos]]=='*':
                auxFirst=self.evalExpression(pos+1,crtData)
                auxSecond=self.evalExpression(auxFirst[1]+1,crtData)
                return auxFirst[0]*auxSecond[0],auxSecond[1]

    def computeFitness(self, crtData,crtOut,noExamples):
        '''
        the fitness function
        '''
        err = 0.0
        for d in range(noExamples):
            err += crtOut[d]-self.evalExpression(0, crtData[d])
        self.fitness = err

    def traverse(self,pos):
        '''
        returns the next index where it begins the next 
        branch in the tree from the same level
        '''
        if (self.repres[pos] > 0):	 #terminal
            return pos+1
        else:
            return self.traverse(self.traverse(pos+1))

def crossover(M,F):
    off=Chromosome()
    while True:
        startM = randint(0,M.size-1)
        endM = M.traverse(startM)
        startF = randint(0,F.size-1)
        endF = F.traverse(startF)
        if (len(off.repres)<endM+(endF-startF-1)+(M.size-endM-1)):
            break
    i=-1
    for i in range(startM):
        off.repres[i] = M.repres[i]
    for j in range(startF, endF):
        i=i+1
        off.repres[i] = F.repres[j]
    for j in range(endM,M.size):
        i=i+1
        off.repres[i] = M.repres[j]
    off.size=i+1
    return off

def mutation(c):
    off=Chromosome()
    pos = randint(0,c.size)
    off.repres = c.repres[:]
    off.size=c.size
    if off.repres[pos] > 0:	#terminal
        off.repres[pos] = randint(1,noTerminals)
    else:	#function
        off.repres[pos] = -randint(1,noFunctions)
    return off
