#!/usr/bin/python3

print("[CALCULANDO A MÁXIMA QUANTIDADE DE CÉDULAS E MOEDAS]\n")

valor = float( input("Insira o valor: ") )

# Calculando a quantidade de notas através do operador de divisão inteira
notas100 = valor // 100
# Atualizando o valor utilizando o operador módulo (resto)
valor = valor % 100

# Repetindo para todas as notas
notas50 = valor // 50
valor = valor % 50

notas20 = valor // 20
valor = valor % 20

notas10 = valor // 10
valor = valor % 10

notas5 = valor // 5
valor = valor % 5

notas2 = valor // 2
valor = valor % 2

notas1 = valor // 1
valor = valor % 1

moedas50 = valor // 0.50
valor = valor % 0.50

moedas25 = valor // 0.25
valor = valor % 0.25

moedas10 = valor // 0.10
valor = valor % 0.10

moedas5 = valor // 0.05
valor = valor % 0.5

moedas1 = valor // 0.01
valor = valor % 0.01

# Imprimindo o resultado para o usuário
print("Quantidade de notas de 100: " + str(notas100) )
print("Quantidade de notas de 50: " + str(notas50) )
print("Quantidade de notas de 20: " + str(notas20) )
print("Quantidade de notas de 10: " + str(notas10) )
print("Quantidade de notas de 5: " + str(notas5) )
print("Quantidade de notas de 2: " + str(notas2) )
print("Quantidade de notas de 1: " + str(notas1) )
print("Quantidade de moedas de 50: " + str(moedas50) )
print("Quantidade de moedas de 25: " + str(moedas25) )
print("Quantidade de moedas de 10: " + str(moedas10) )
print("Quantidade de moedas de 5: " + str(moedas5) )
print("Quantidade de moedas de 1: " + str(moedas1) )
