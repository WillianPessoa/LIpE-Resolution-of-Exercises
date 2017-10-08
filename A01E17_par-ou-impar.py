#!/usr/bin/python3

print("[VERIFICANDO SE UM NÚMERO É PAR OU ÍMPAR]\n")

num = int( input("Insira um número: ") )

if (num % 2 == 0):
    print("%d é par" % num)
else:
    print("%d é ímpar" % num)
