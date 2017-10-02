#!/usr/bin/python3

print("[CALCULANDO IMPOSTO DE RENDA]\n")

print("Regras para o cálculo do imposto de renda:\n")
print("Salário menor ou igual a $2.000,00  -> não há imposto de renda;")
print("Salário maior que $2.000,00 e menor ou igual a $5.000 -> imposto de renda de 5%;")
print("Salário maior que $5.000,00 e menor ou igual a $10.000 -> imposto de renda de 7,5%;")
print("Salário maior que $10.000,00 e menor ou igual a $15.000 -> imposto de renda de 10%;")    
print("Salário maior que $15.000,00 -> imposto de renda de 15%;\n")

salario = float( input("Insira o salário: ") )

taxaDeImposto = 0

if salario <= 2000:
    taxaDeImposto = 0
elif salario < 5000:
    taxaDeImposto = 0.05
elif salario < 10000:
    taxaDeImposto = 0.075
elif salario < 15000:
    taxaDeImposto = 0.1
else:
    taxaDeImposto = 0.15

print("A taxa de imposto para o salário de R$ %.2f é de %.1f%%" % (salario, taxaDeImposto*100))
print("Com essa taxa, o imposto de renda fica com R$ %.2f do salário" % (salario * taxaDeImposto))
