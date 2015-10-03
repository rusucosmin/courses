a = int(input('give a '))
b = int(input('give b '))
while b != 0:
    a, b = b, a%b
print(a)
