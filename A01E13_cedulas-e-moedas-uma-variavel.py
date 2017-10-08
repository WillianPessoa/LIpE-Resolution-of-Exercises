#!/usr/bin/python3

print("[CALCULANDO A MÁXIMA QUANTIDADE DE CÉDULAS E MOEDAS]\n")

# A única variável necessária é a variável valor
valor = float( input("Insira o valor: ") )

# Em vez de armazenar a quantidade de notas, imprimos essa informação direto
print("Quantidade de notas de 100: " + str(valor // 100) )
# Atualizando o valor utilizando o operador módulo (resto)
valor = valor % 100

# Repetindo para todas as notas e moedas
print("Quantidade de notas de 50: " + str(valor // 50) )
valor = valor % 50

print("Quantidade de notas de 20: " + str(valor // 20) )
valor = valor % 20

print("Quantidade de notas de 10: " + str(valor // 10) )
valor = valor % 10

print("Quantidade de notas de 5: " + str(valor // 5) )
valor = valor % 5

print("Quantidade de notas de 2: " + str(valor // 2) )
valor = valor % 2

print("Quantidade de notas de 1: " + str(valor // 1) )
valor = valor % 1

print("Quantidade de moedas de 50: " + str(valor // 0.50) )
valor = valor % 0.50

print("Quantidade de moedas de 25: " + str(valor // 0.25) )
valor = valor % 0.25

print("Quantidade de moedas de 10: " + str(valor // 0.10) )
valor = valor % 0.10

print("Quantidade de moedas de 5: " + str(valor // 0.05) )
valor = valor % 0.5

print("Quantidade de moedas de 1: " + str(valor // 0.01) )
valor = valor % 0.01
