#!/usr/bin/python3

# int() é utilizado para converter o texto inserido em número inteiro.
base = int( input("Insira o valor da base em cm: ") )
lado= int( input("Insira o valor da altura em cm: ") )

# Calculando a area
area = lado * altura

# %d é substituído pelo valor da variável área no formato inteiro
print ("A área do quadrilátero (quadrado ou retangulo) é %d cm²" % area)
