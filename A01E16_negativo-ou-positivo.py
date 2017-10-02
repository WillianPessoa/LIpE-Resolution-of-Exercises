#!/usr/bin/python3

print("[VERIFICANDO SE UM NÚMERO É NEGATIVO, POSITIVO OU NEUTRO]\n")

num = int( input("Insira um número: ") )

if (num < 0):
    print("%d é negativo" % num)
elif (num > 0):
    print("%d é positivo" % num)
else:
    print("%d é neutro")
