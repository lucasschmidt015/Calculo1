import math

def equacao(x):
    conta = x**3 +x**2 + math.sin(x) -2
    return conta

def meio(a=None, b=None):
    meio = (a - b)/2
    return meio

a = int(input())
b = int(input())
distancia = a - b
contador = 0
#while distancia > 0.1:
Img1 = equacao(a)
Img2 = equacao(b)
pmeio = meio(a,b)
ImgM = equacao(pmeio)
b = pmeio
if ImgM < 0 and Img1 > 0:
    b = pmeio
    print("A")
    contador+=1
elif ImgM < 0 and Img2 > 0:
    a = pmeio
    contador+=1
    print("B")
elif ImgM > 0 and Img1 < 0:
    b = pmeio
    print("C")
    contador+=1
elif ImgM > 0 and Img2 < 0:
    a = pmeio
    print("D")
    contador+=1
else:
    print("não é possível afirmar que existe solução neste intervalo, tente outros dois números")
    distancia = a - b

 
