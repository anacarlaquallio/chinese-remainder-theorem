import numpy as np
import sys
from decimal import Decimal

def equation_solver(a:int, b:int, n:int):
    mdc, x, _ = extended_gcd_iterative(a, n)

    if ((b % mdc) == 0):
        x0 = (x*(b//mdc)) % n
        i = 0
        while (i <= mdc - 1):
            print("Possível solução para x: ", (x0 + i*(n//mdc)) % n)
            i += 1
    else:
        print("Nenhuma solução!")

def verifica(x: np.ndarray, a: np.ndarray, b:np.ndarray):
    for i in range(len(x)):
        if x[i] != 1:
            j = modulo_inverse(x[i], b[i])
            if (j == -1):
                print("O sistema não possui solução!")
                sys.exit()
            a[i] = (a[i] * j) % b[i]  
    return chinese_remainder(a, b)

def extended_gcd_iterative(a:int, b:int):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modulo_inverse(a:int, m:int):
    d, x, _ = extended_gcd_iterative(a, m)
    if d != 1:
        return -1
    else:
        return x % m

def chinese_remainder(a:np.ndarray, b:np.ndarray):
    
    n2 = len(b)
    M = np.zeros(n2, dtype=Decimal)
    M_barra = np.zeros(n2, dtype=Decimal)
    M_inverso = np.zeros(n2, dtype=Decimal)
    produto = np.zeros(n2, dtype=Decimal)

    for i in range(n2):
        temp_produto = 1
        for j in range(n2):
            if i != j:  # Evite multiplicar a linha atual
                temp_produto *= b[j]
        M[i] = temp_produto
    
    M_barra = [M[i] % b[i] for i in range(n2)]
 
    for i in range(n2):
        j = modulo_inverse(M_barra[i], b[i])
        if j == -1: 
            print("O sistema não possui solução!")
            sys.exit()
        else:
            M_inverso[i] = j

    soma = 0
    produto_mod = 1
    for i in range(n2):
        produto[i] = a[i] * M[i] * M_inverso[i]
        soma += produto[i]
        produto_mod *= b[i]
    
    return soma % produto_mod, produto_mod

print("Este algoritmo resolve um sistema modular da forma:")
print("x ≡ a1 (mod b1)")
print("x ≡ a2 (mod b2)")
print("...")
print("x ≡ an (mod bn)\n")

n = int(input("Digite o número de equações: "))
if n == 1:
    m = int(input("Digite o coeficiente m da equação: "))
    a = int(input("Digite o coeficiente a da equação: "))
    b = int(input("Digite o coeficiente b da equação: "))
    equation_solver(m, a, b)
else:
    m = np.zeros(n, dtype=Decimal)
    a = np.zeros(n, dtype=Decimal)
    b = np.zeros(n, dtype=Decimal)
    for i in range(n):
        m[i]= int(input(f"Digite o coeficiente x da equação {i+1}: "))
        a[i] = int(input(f"Digite o coeficiente a da equação {i+1}: "))
        b[i] = int(input(f"Digite o coeficiente b da equação {i+1}: "))

    result, mod = verifica(m, a, b)
    print(f"Solução: {result} (mod {mod})")