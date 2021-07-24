import math

def equacao(x):
    return x**3 +x**2 + math.sin(x) -2


def meio(a=None, b=None):
    meio = (a - b)/2
    return meio

'''def bissecao(f,a,b,prec):
    """ Método da bisseção para uma função f no intervalo [a,b]. """
    m = (a+b)/2
    # Se já há precisão suficiente, retornamos o ponto médio do intervalo
    if abs(b - a) < prec: 
        return m
    # Se f(m) == 0, achamos uma raiz exata!
    if f(m) == 0: return m'''

parar = 10e-1
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
    Img1 = equacao(a)
    Img2 = equacao(b)
    pmeio = meio(a,b)
    ImgM = equacao(pmeio)
    b = pmeio
    if ImgM < 0 and Img1 > 0 or ImgM > 0 and Img1 < 0:
        print(ImgM, "  A ", Img1)
        b = pmeio
        print("A")
        contador+=1
    elif ImgM < 0 and Img2 > 0 or ImgM > 0 and Img2 < 0:
        print(ImgM, " B  ", Img2)
        a = pmeio
        contador+=1
    distancia = a - b
    print(f"Distancia: {distancia:.4f}")
    if abs(distancia) < parar:
        print(parar)
        break

 
