#!/usr/bin/python3

print("[VERIFICANDO SE UM NÚMERO É NEGATIVO, POSITIVO OU NEUTRO")
print("E TAMBÉM SE É PAR OU ÍMPAR]\n")

num = int( input("Insira um número: ") )

sinal = ""
paridade = ""

# Identificando o sinal
if num < 0:
    sinal = "negativo" 
elif num > 0:
    sinal = "positivo"
else:
    sinal = "neutro"

# Identificando a paridade
if num % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

print ("%d é %s e %s" % (num, sinal, paridade))
