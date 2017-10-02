#!/usr/bin/python3

print ("[CALCULANDO O VOLUME DE UMA ESFERA ATRAVÉS DE SEU RAIO]\n")

PI = 3.14159    

# int() é utilizado para converter o texto inserido em número inteiro.
raio = int( input("Insira o valor do raio em cm: ") )

# Calculando o volume
volume = (3/4) * PI * (raio**3)

# %d é substituído pelo valor da variável volume no formato inteiro
print ("A volume do círculo é %d cm³" % volume)
