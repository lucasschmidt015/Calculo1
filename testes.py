'''entrada1=float(input("Digite o primeiro valor do intervalo: "))
entrada2=float(input("Digite o segundo valor do intervalo: "))
if entrada1 > 0 and entrada2 < 0 or entrada1 < 0 and entrada2 >0:
    print("a equação tem pelo menos uma solução neste intervalo")
else:
    print("nada")'''

import math

def equacao(x): #funcao que retorna f(x)
   y = x**3 +x**2 + math.sin(x) -2
   return y

def meio(a=None, b=None): #retorna o meio da reta x entre os valores de entrada
    meio = (a - b)/2
    return meio


def verificar(y1, y2, meio):
    if(y1 < meio > y2 or y1 > meio < y2):
        return False
    elif(meio > 0 and y2 < 0 or meio < 0 and y2 > 0):
        return y2
    elif(meio < 0 and y1 > 0 or meio > 0 and y1< 0):
        return y1


while True:
    x1 = float(input())
    x2 = float(input())
    y1 = equacao(x1)
    y2 = equacao(x2)
    if(verificar(y1, y2, 0)):
        print("não é possível afirmar que existe solução neste intervalo, tente outros dois números")
    else:
        meio = meio(x1, x2)
        meio = equacao(meio)
        print(meio)
        break