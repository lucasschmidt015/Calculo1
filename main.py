def f(a):
    from math import sin
    return a**3 +a**2 + sin(a) -2

def meio(a=None, b=None):
    return (a + b)/2

parar = 10**-9
digte_num = True
print("*"*11,"Funcao","*"*11)
print("x**3 + x**2 +sen(x) -2".center(30))
print("*"*30)
while True:
    while digte_num:
        a = float(input("Ponto 1: "))
        b = float(input("Ponto 2: "))
        if(f(a) > 0 < f(b) or f(a)< 0 > f(b)):
            print("não é possível afirmar que existe solução neste intervalo, tente outros dois números")
        else:
            digte_num = False
    Img1 = f(a)
    Img2 = f(b)
    pmeio = meio(a,b)
    ImgM = f(pmeio)
    if ImgM < 0 and Img1 > 0 or ImgM > 0 and Img1 < 0:
        b = pmeio
    elif ImgM < 0 and Img2 > 0 or ImgM > 0 and Img2 < 0:
        a = pmeio
    if abs(ImgM) < parar:
        print(f"a reta tem pelo menos uma solução neste intervalo")
        print(f"Menor intervalo: [{a}, {b}]")
        quit = input("Quer continuar? [S/N]: ").upper()
        if quit == 'N':
            break
        else:
            digte_num = True
