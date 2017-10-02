#!/usr/bin/python3

print("[RESOLVENDO UMA EQUAÇÃO DE PRIMEIRO GRAU]\n")

# Formato da equação de primeiro grau: ax + b = c
# Precisamos encontrar o valor de X
# Para isso, precisamos do valor de a, b e c

a = int( input("Insira o valor de A: ") )
b = int( input("Insira o valor de B: ") )
c = int( input("Insira o valor de C: ") )

# Na equação de primeiro grau, sempre passamos "b" e "a" para o lado de C
# invertendo o sinal. Fazemos a mesma coisa.

c = c - b   # "b vai pra lá subtraindo"
c = c / a   # "a vai pra lá dividindo"

# X = C

print ("O valor de X é %d." % c)

