import os

os.system("cls")

print("= Solicitando da dados =")
ano_nacimento = int(input("Digite o ano de nascimento: "))

def calcular_idade(ano):
    idade = 2026 - ano
    print(f"Idade: {idade}")
    

    print("= solicitando da dados =")
ano_nacimento = int(input("Digite o ano de nascimento: "))

# Chamando a função para calcular a idade
idade = calcular_idade(ano_nacimento)

print("n\ exibindo resultado =")
print(f"Idade: {idade}")