#!/usr/bin/python3

print("[CALCULANDO A MÁXIMA QUANTIDADE DE CÉDULAS]\n")

valor = int( input("Insira o valor: ") )

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

# Imprimindo o resultado para o usuário
print("Quantidade de notas de 100: " + str(notas100) )
print("Quantidade de notas de 50: " + str(notas50) )
print("Quantidade de notas de 20: " + str(notas20) )
print("Quantidade de notas de 10: " + str(notas10) )
print("Quantidade de notas de 5: " + str(notas5) )
print("Quantidade de notas de 2: " + str(notas2) )
print("Quantidade de notas de 1: " + str(notas1) )
