#!/usr/bin/python3

print("[RESOLVENDO UMA EQUAÇÃO DE SEGUNDO GRAU]\n")

# Formato da equação de segundo grau: ax² + bx + c = 0
# Precisamos encontrar o valor de X1 e X2
# Para isso, precisamos do valor de a, b e c

a = int( input("Insira o valor de A: ") )
b = int( input("Insira o valor de B: ") )
c = int( input("Insira o valor de C: ") )

# Resolvemos isso com Bháskara
# Vamos começar calculando DELTA 

delta = (b**2) - (4 * a * c)

# Agora iremos calcular as raízes (x1 e x2) da função
# Precisamos declarar as variáveis no escopo global 
x1 = 0
x2 = 0

# Se delta for negativo, a função não tem solução. Pois não podemos calcular
# a raiz de um número negativo.
if (delta < 0):
    print("A equação não tem solução real, pois delta é negativo")
    print("Valor de delta %d" % delta)
else:
    x1 = ((-b) + (delta ** 0.5)) / (2 * a)      # Elevar a meio == raiz
    x2 = ((-b) - (delta ** 0.5)) / (2 * a)      
    print("Valor de X1: " + str(x1))
    print("Valor de X2: " + str(x2))

