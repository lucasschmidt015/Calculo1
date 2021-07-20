'''entrada1=float(input("Digite o primeiro valor do intervalo: "))
entrada2=float(input("Digite o segundo valor do intervalo: "))
if entrada1 > 0 and entrada2 < 0 or entrada1 < 0 and entrada2 >0:
    print("a equação tem pelo menos uma solução neste intervalo")
else:
    print("nada")'''

import math

def equacao(x):
   y = x**3 +x**2 + math.sin(x) -2
   return y

x1 = float(input())
x2 = float(input())
y1 = equacao(x1)
y2 = equacao(x2)
print(y1, y2)
if y1 > 0 < y2:
    print("não é possível afirmar que existe solução neste intervalo, tente outros dois números")
#else:
    