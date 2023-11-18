import inverso as iv
import numpy as np
import sys
from decimal import Decimal

def equation_solver(a:int, b:int, n:int):
    mdc, x, _ = iv.mdc_extendido(a, n)
    
    if ((b % mdc) == 0):
        x0 = (x*(b//mdc)) % n
        i = 0
        while (i <= mdc - 1):
            print("Possível solução para x: ", (x0 + i*(n//mdc)) % n)
            i += 1
    else:
        print("Nenhuma solução!")


def corte(m:int, a:int, b:int):
    mdc, i, _ = iv.mdc_extendido(m, b)
    if mdc != 1:
        if (a % mdc == 0):
            return m//mdc, a//mdc, b//mdc
        else: return -1, -1, -1
    else:
        return (m*i)%b, (a*i)%b, b  

def coprime(num1:int, num2:int):
    mdc, _, _ = iv.mdc_extendido(num1, num2)
    return (mdc==1)

def inverso (b: int, d: int):
    mdc, x, _ = iv.mdc_extendido(b, d)

    if (mdc != 1):
            b = b // mdc
            d = d // mdc
    
    if (x < 0):
        x = d + x        
    return x, b, d, mdc
        
def calcula_equacao (m:int, n:int, a:int, b:int, c:int, d:int):
    if (m == 0 or n == 0):
        return 0, 0

    if (m != 1):
        m, a, b = corte(m, a, b)
        if a == -1:
            return 0, 0
    
    if (n != 1):
        n, c, d = corte(n, c, d)
        if c == -1:
            return 0, 0

    i, b, d, mdc = inverso(b, d)
    if mdc != 1:
        if not((c-a)%mdc == 0): 
            return 0, 0

    x = (i * b * (c - a) + a)
    gama = b * d * mdc

    if x < 0:
        x = gama + x

    return x % gama, gama

print("Este algoritmo resolve um sistema modular da forma:")
print("m1*x ≡ a1 (mod b1)")
print("m2*x ≡ a2 (mod b2)")
print("...")
print("mn*x ≡ an (mod bn)\n")

# Solicitar o número de equações
n = int(input("Digite o número de equações: "))

if n == 1:
    m = int(input("Digite o coeficiente m da equação: "))
    a = int(input("Digite o coeficiente a da equação: "))
    b = int(input("Digite o coeficiente b da equação: "))

    # Chamar a função equation_solver com uma única equação
    equation_solver(m, a, b)

else:
    matriz = np.zeros((n, 3), dtype=Decimal)
    solucoes = np.zeros((n // 2, 3), dtype=Decimal)
    ultima = np.zeros((1, 3), dtype=Decimal)
    bi = np.zeros((n), dtype=Decimal)

    # Preencher a matriz com os coeficientes das equações
    for i in range(n):
        m = int(input(f"Digite o coeficiente m da equação {i+1}: "))
        a = int(input(f"Digite o coeficiente a da equação {i+1}: "))
        b = int(input(f"Digite o coeficiente b da equação {i+1}: "))
        if b == 0:
            print("O número que acompanha mod precisa ser positivo!")
            sys.exit()
        else:
            matriz[i] = [m, a, b]
            bi[i] = b
            if n % 2 != 0: 
                ultima[0] = matriz[-1].copy()

    i = 0
    while i+1 < n:
        eq1 = matriz[i]
        eq2 = matriz[i+1]
        m1, a1, b1 = eq1
        m2, a2, b2 = eq2
        x, gama = calcula_equacao(m1, m2, a1, b1, a2, b2)
        solucoes[i // 2] = [1, x, gama]
        if x == 0 and gama == 0:
            print("O sistema não possui solução!")
            sys.exit()
        i +=2
    if n % 2 != 0: resultado = np.concatenate((solucoes, ultima), axis=0)
    else: resultado = solucoes
    while len(resultado) > 1:
        new_resultado = []
        i = 0
        while i < len(resultado):
            if i+1 < len(resultado):
                eq1 = resultado[i]
                eq2 = resultado[i+1]
                m1, a1, b1 = eq1
                m2, a2, b2 = eq2
                x, gama = calcula_equacao(m1, m2, a1, b1, a2, b2)
                if x == 0 and gama == 0:
                    print("O sistema não possui solução!")
                    sys.exit()
                new_resultado.append([1, x, gama])
            else:
                new_resultado.append(resultado[i])
            i += 2
        resultado = new_resultado.copy()
   
    # Imprime resultado final
    print(f'Possível solução que satisfaz as equações: x ≡ {int(resultado[0][1])} mod ({int(resultado[0][2])})') 