#A = { a E Z | i = 1,n }
#B inc A : Sum(bi) (i=1,m) = S

#reprezentare
#fitness
#operators
#selection
#stop condition 

#pi 	= 0, if ai !E B
#	= 1, if ai E B

# fitness f(p) = | SUM(pi * ai - S |, i in range(1,n)

# operators
# crossover
# mutation 

# selection : elitist

# stop condition - max. generation


import random

class Problem:
	def __init__(self, fname):
		self.n = 100
		self.A = [i for i in range(1,101)]
		self.S = 520
		self.filename = fname
		#self.load()
	
	# def load(self):
	# 	//TODO

class Individual:
	def __init__(self, p):
		self.size = p.n
		self.v = [random.sample([0,1],1)[0] for k in xrange(self.size)]
		self.summ = 0
		self.f = 0

	def fitness(self, p):
		self.summ = sum([p.A[k]*self.v[k] for k in xrange(self.size)])
		self.f = abs(p.S - self.summ)

class Population:
	def __init__(self, noInd, p):
		self.psize = noInd
		self.pop = [Individual(p) for k in xrange(self.psize)]

	def evaluate(self,p):
		for x in self.pop:
			x.fitness(p)

	def reunion(self, toAdd):
		self.psize = self.psize + toAdd.psize
		self.pop = self.pop + toAdd.pop

	def selection(self, n):
		if n < self.psize:
			self.pop = sorted(self.pop, key = lambda Individual: Individual.f)
			self.pop = self.pop[:n]
			self.psize = n
	
	def best(self, n):
		aux = sorted(self.pop, key = lambda Individual: Individual.f)
		return aux[:n]

class Algorithm:
	def __init__(self, noI = 100, noG = 100, fname="date.in"):
		self.p = Problem(fname)
		self.noInd = noI
		self.noGen = noG
		self.population = Population(self.noInd, self.p)
		self.population.evaluate(self.p)

	def iteration(self):
		indexes = range(self.noInd)
		random.shuffle(indexes)
		no = self.noInd // 2
		offspring = Population(no, self.p)
		for k in xrange(no):
			offspring.pop[k].v = self.crossover(self.population.pop[indexes[k*2]], self.population.pop[indexes[k*2+1]])
			self.mutate(offspring.pop[k])
		offspring.evaluate(self.p)
		self.population.reunion(offspring)
		self.population.selection(self.noInd)

	def run(self):
		for k in xrange(self.noGen):
			self.iteration()
		return self.population.best(1)

	def crossover(self,i1,i2):
		aux = []
		for k in xrange(i1.size):
			if(random.random() < 0.5):
				aux.append(i1.v[k])
			else:
				aux.append(i2.v[k])
		return aux

	def mutate(self, ind):
		if random.random() < 0.1:
			k = random.randint(0, ind.size-1)
			ind.v[k] = 1 - ind.v[k]


if __name__ == "__main__":
	alg = Algorithm()
	result = alg.run()
	s = 0
	for i in range(len(result[0].v)):
		if result[0].v[i] != 0:
			s+=i+1
			print i+1, 

	print 'sum', s,







































