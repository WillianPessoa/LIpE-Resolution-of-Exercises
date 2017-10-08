#!/usr/bin/python3

print("[VALIDADOR DE DATA]\n")

dia = int( input("Insira o dia: ") )
mes = int( input("Insira o mês: ") )
ano = int( input("Insira o ano: ") )

validade = True          # Partiremos do presuposto que a data é válida
                            # E testaremos essa validade no decorrer do código

# Identificando se o ano é válido e se é bissexto
bissexto = False
if ano < 0:                 # Se o ano for negativo, indentificamos a invalidade da data
    validade = False            
else:                       # Se não for negativo, seguimos com as verificações
    if ano % 4 == 0:            # Primeiro, verifico se o ano é divisível por 4
        if ano % 100 != 0:      # Depois, verifico se o ano não é divísivel por 100
            bissexto = True         # Se não for divisível, é bissexto
        elif ano % 400 == 0:    # Se for divísivel por 100, verifico se é divisível por 400
            bissexto = True         # Se for divisível por 400, é bissexto


# Identificando o número máximo de dias para o mês em questão
# Também verifico se o mês é válido
maxDias = 0

if validade:                # Se a data for válida, faça as verificações
    if mes <= 0:                 # Se o mês for negativo ou nulo
        validade = False            # Identificamos a data como inválida
    elif mes <= 7:              # Se o mês não for negativo ou nulo, verificamos se o mês é menor ou igual ao mês 7
        if mes == 2:                # Se o mês for o mês 2 (fevereiro)
            if bissexto:                # Verificamos se o ano é bissexto
                maxDias = 29                # Número máximo de dias é 29
            else:                       # Se não for bissexto,
                maxDias = 28                # Número máximo de dias é 28
        elif mes % 2 == 0 :          # Se não foro mês de fevereiro, verificamos se é um mês par,
            maxDias = 30                # Número máximo de dias é 30
        else:                       # Se o mês não for um mês par, ou seja, se for ímpar
            maxDias = 31                # Número máximo de dias é 31
    elif mes <= 12:             # Se for um mês maior que o mês 7 e menor que o mês ou igual 12
        if mes % 2 == 0:            # Se for um número de mês par
            maxDias = 31                # Número de dias máximos é 30
        else:                       # Se não for mês par, ou seja, for ímpar
            maxDias = 30                # Número de dias máximo é 31
    else:                       # Se for um mês maior que 12
        validade = False            # Identificamos a data com inválida

# Verificando se o dia está entre o número mínimo e máximo de dias
if validade:    # Antes, verificamos se a data continua sendo válida
    if dia < 0:
        validade = False
    elif dia > maxDias:
        validade = False


# Imprimindo a mensagem de acordo com a validade
if validade:
    print("Data válida!")
else:
    print("Data inválida")
        
    
        
