#!/usr/bin/python3

print("[CALCULANDO O ÍNDICE DE MASSA CORPORAL (IMC)]\n")

print("Classificações para cada faixa de IMC:\n")
print("\tAbaixo de 18,5 Abaixo do peso;")
print("\tEntre 18,5 e 25 Peso normal;")
print("\tEntre 25 e 30 Acima do peso;")
print("\tAcima de 30 obeso.\n")

altura = float( input("Insira a altura em metros: ") )
peso = float ( input("Insisra o peso em kg: ") )

# Calculando a taxa IMC
imc = peso / (altura**2)


# Classificando o IMC conforme a taxa
classificacao = ""
if imc <= 18.5:
    classificacao = "abaixo do peso"
elif imc <= 25:
    classificacao = "peso normal"
elif imc <= 30:
    classificacao = "acima do peso"
else:
    classificacao = "obeso"

print("IMC: %.1f" % imc)
print("Classificação: " + classificacao) 
    
