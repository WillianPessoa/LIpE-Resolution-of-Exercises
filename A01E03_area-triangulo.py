#!/usr/bin/python3

# int() é utilizado para converter o texto inserido em número inteiro.
base = int( input("Insira o valor da base em cm: ") )
altura = int( input("Insira o valor da altura em cm: ") )

# Calculando a area
area = base * altura

# %d é substituído pelo valor da variável área no formato inteiro
print ("A área do triângulo é %d cm²" % area)
