#!/usr/bin/python3

# float() é utilizado para converter o texto inserido em número real/fracionário.
nota1 = float( input("Insira a nota da primeira prova: ") )
nota2 = float( input("Insira a nota da segunda prova: ") )
nota3 = float( input("Insira a nota da terceira prova: ") )

# Calculando a média das notas das provas
media =  (nota1 + nota2 + nota3) / 3

# %2.f é substituído pelo valor da média com a precisão de duas casas decimais
print ("A media das três provas é %.2f" % media)
