import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def classificar_imc(imc):
    if imc <= 18.5:
        return "Abaixo do peso"
    elif imc <= 24.9:
        return "Peso normal"
    elif imc <= 29.9:
        return "Sobrepeso"
    elif imc <= 34.9:
        return "Obesidade grau I"
    elif imc <= 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    imc = peso / (altura ** 2)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuario {i+1}:")
    print("Nome:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print("IMC:", round(imc, 2))
    print("Classificação do IMC:", classificar_imc(imc))
    print()