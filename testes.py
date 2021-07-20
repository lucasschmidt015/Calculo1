'''entrada1=float(input("Digite o primeiro valor do intervalo: "))
entrada2=float(input("Digite o segundo valor do intervalo: "))
if entrada1 > 0 and entrada2 < 0 or entrada1 < 0 and entrada2 >0:
    print("a equação tem pelo menos uma solução neste intervalo")
else:
    print("nada")'''

import math

x1 = float(input())
x2 = float(input())
conta1 =x1**3 +x1**2 + math.sin(x1) -2
conta2 =x2**3 +x2**2 + math.sin(x2) -2
print(conta1, conta2)
if conta1 > 0 and conta2 < 0 or conta1 < 0 and conta2 > 0:
    print("a equação tem pelo menos uma solução neste intervalo")
else:
    