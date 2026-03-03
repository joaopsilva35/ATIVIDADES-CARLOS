import os 

os.system("cls")
#ENTRADA DE DADOS

matricula = input("Digite a sua matricula: ")

ano_nacimento = int(input("Digite seu ano de nascimento: "))

tempo_de_trabalho = int(input("Digite o tempo de tempo de trabalho em anos"))

#PROCESSAMENTO
idade = 2026 - ano_nacimento

if idade >= 65:
    resultado = "requerer aposentadoria"

else:
    idade >= 30:
    resultado = "nao requer aposentadoria"

