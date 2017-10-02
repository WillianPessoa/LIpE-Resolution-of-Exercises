#!/usr/bin/python3

print("[CALCULANDO O CONSUMO DE COMBUSTÍVEL DE UM AUTOMÓVEL]\n")

distancia = float( input("Distancia percorrida: ") )
consumoMedio = float( input("Consumo médio do veículo (litros/km): ") )
valorCombustivel = float( input("Cotação do combustível (em R$): " ) )

consumoTotal = consumoMedio * distancia
despesaCombustivel = consumoTotal * consumoTotal

print("Foram consumidos %.1f litros de combutível" % consumoTotal)
print("E a despesa com combustível foi de R$ %.2f" % despesaCombustivel)
