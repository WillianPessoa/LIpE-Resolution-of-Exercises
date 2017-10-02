#!/usr/bin/python3

print("[IDENTIFICANDO OBRIGATÓRIEDADE, OPTATIVIDADE OU PROIBIÇÃO PARA VOTAR]\n")

idade = int( input("Insira a idade: ") )

condicao = "" 

# Verificando se é menor de 16
if idade < 16:      
    condicao = "proíbida"
# Verificando se é menor de 18 (sabemos que é maior ou igual a 16)
elif idade < 18:    
    condicao = "optativa"
# Verificando se é maior ou igual de 18 (sabemos que é maior ou igual a 18)
elif idade < 65:    
    condicao = "obrigatória"
# Sabemos que é maior ou igual a 65
else:
    condicao = "optativa"

print("Cidadãos com %d anos tem a condição de voto %s" % (idade, condicao))
      


    
