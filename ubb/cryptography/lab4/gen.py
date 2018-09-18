from random import randint

T = 10
LB = [10,  10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10]
UB = [100, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**11]

for i in range(T):
  with open("tests/" + str(i + 1) + ".in", "w") as f:
    f.write(str(randint(LB[i], UB[i])) + "\n")
