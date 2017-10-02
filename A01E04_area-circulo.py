#!/usr/bin/python3

# A única vez que nomeamos uma variável com suas letras maiúsculas é quando
# sabemos que essa variável não vai mudar de valor (CONSTANTE)
PI = 3.14159    

# int() é utilizado para converter o texto inserido em número inteiro.
raio = int( input("Insira o valor do raio em cm: ") )

# Calculando a area
area = PI * (raio**2)

# %d é substituído pelo valor da variável área no formato inteiro
print ("A área do círculo é %d cm²" % area)
