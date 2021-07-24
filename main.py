import math

def f(x):
    return x**3 +x**2 + math.sin(x) -2


def meio(a=None, b=None):
    meio = (a + b)/2
    return meio


parar = 10**-1
contador = 0
digte_num = True
distancia = float
while True:
    while digte_num:
        a = float(input())
        b = float(input())
        if(a > 0 < b or a< 0 > b):
            print("não é possível afirmar que existe solução neste intervalo, tente outros dois números")
        else:
            digte_num = False
    Img1 = f(a)
    Img2 = f(b)
    pmeio = meio(a,b)
    ImgM = f(pmeio)
    b = pmeio
    if ImgM < 0 and Img1 > 0 or ImgM > 0 and Img1 < 0:
        print(Img1, "  A ", ImgM)
        b = pmeio
        print("A")
        contador+=1
    elif ImgM < 0 and Img2 > 0 or ImgM > 0 and Img2 < 0:
        print(ImgM, " B  ", Img2)
        a = pmeio
        contador+=1
    distancia = a - b
    print(f"Distancia: {distancia:.4f}")
    if abs(b - a) < parar:
        break

 
