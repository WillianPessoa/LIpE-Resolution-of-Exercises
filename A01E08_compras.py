#!/usr/bin/python3

print("[CALCULANDO O VALOR DA COMPRA DE 5 PRODUTOS]\n")

produto1 = input("Insira o nome do primeiro produto: ")
quantidade1 = int( input("Insira quantidade deste produto: "))
preço1 = float( input("Insira o preço deste produto: "))

print() # Apenas para o programa pular uma linha

produto2 = input("Insira o nome do segundo produto: ")
quantidade2 = int( input("Insira quantidade deste produto: "))
preço2 = float( input("Insira o preço deste produto: "))

print()

produto3 = input("Insira o nome do terceiro produto: ")
quantidade3 = int( input("Insira quantidade deste produto: "))
preço3 = float( input("Insira o preço deste produto: "))

print()

produto4 = input("Insira o nome do quarto produto: ")
quantidade4 = int( input("Insira quantidade deste produto: "))
preço4 = float( input("Insira o preço deste produto: "))

print()

produto5 = input("Insira o nome do quinto produto: ")
quantidade5 = int( input("Insira quantidade deste produto: "))
preço5 = float( input("Insira o preço deste produto: "))

print()

totalProduto1 = preço1 * quantidade1
totalProduto2 = preço2 * quantidade2
totalProduto3 = preço3 * quantidade3
totalProduto4 = preço4 * quantidade4
totalProduto5 = preço5 * quantidade5
total = totalProduto1 + totalProduto2 + totalProduto3 + totalProduto4  + totalProduto5  

print ("RESUMO DAS COMPRAS:")
print ("%s - R$ %.2f" % (produto1, totalProduto1))
print ("%s - R$ %.2f" % (produto2, totalProduto2))
print ("%s - R$ %.2f" % (produto3, totalProduto3))
print ("%s - R$ %.2f" % (produto4, totalProduto4))
print ("%s - R$ %.2f" % (produto5, totalProduto5))
print ("O total gasto com estes produtos foi R$ %.2f" % total)


