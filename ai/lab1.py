'''
Aims:
To perform a random search for a given problem, to compute a quality measure for the
solution candidates, to make some statistical analysis to a sample set of possible solutions.
Task:
Develop an application in python that has the following functionalities:
1. Randomly creates possible solutions for your assigned problem (Random Candidate
Solution Generator) (25p).
2. Check if a candidate to the solution is indeed a viable solution (25p).
3. Assigns a measure of quality (a positive value) to a candidate solution - where zero
marks a correct one and, as the candidate is more and more farther from the correct
solution the number grows (Fitness Function) (25p).
4. For a sample set (of size n) of random generated solutions, the mean and the standard
deviation of their quality measures is computed (25p)



11. Caravan
A caravan of n camels is traveling through desert in a single line. To break the monotony
of the long traveling days, each other day the camels are settled so it doesn't see the
same camel in front of her before. Generate possibilities to arrange the camels, knowing
how were place in the first day



Solution:
    - initially, suppose the camles were arranged
        0, 1, 2, .. n - 1 (so it's easier)

    - A candidate solution is any possible permutation of
        - the camels (no need for check if a solution is valid)

    - A fitness function can be:
        - nr of camels - nr of camels that see another camel in from - 1
'''

import numpy
import random

def generate_camels(n):
    x = range(n)
    random.shuffle(x)
    return x

def fitness_function(p):
    cnt = len(p) - 1
    for i in range(len(p) - 1):
        if p[i] + 1 != p[i + 1]:
            cnt -= 1
    return cnt

def generate_samples(n, m):
    samples = [generate_camels(n) for _ in range(m)]
    fitness = [fitness_function(x) for x in samples]
    print("\n".join([str(samples[i]) + " fitness = " + str(fitness[i]) for i in range(len(samples))]))
    print("mean: %.6f" % numpy.mean(fitness))
    print("std dev: %.6f" % numpy.std(fitness))

def main():
    n = int(input("number of camles: = "))
    m = int(input("sample size: = "))
    generate_samples(n, m)

main()
