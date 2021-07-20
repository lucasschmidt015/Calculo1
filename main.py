import math

def equacao(x):
    if x <0:
        for i in range(x, 0):
            conta =i**3 +i**2 + math.sin(i) -2
            print(conta)
    else:
        for i in range(0, x+1):
            conta =i**3 +i**2 + math.sin(i) -2
            print(conta)

a = int(input())
b = int(input())
equacao(a)
equacao(b)