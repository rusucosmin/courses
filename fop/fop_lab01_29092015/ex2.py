n = int(input())
print ('the first prime number larger than ' + str(n))
while True:
    i = 2
    print(n)
    prime = True
    while i * i <= n and prime:
        if n % i == 0:
            prime = False;
        i += 1 
    if prime == True:
        break
    n += 1
print (n)
