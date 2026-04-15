import os

os.system("cls")

# Variáveis para armazenar os números
numero1 = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))
numero3 = int(input("Digite o 3º número: "))
numero4 = int(input("Digite o 4º número: "))
numero5 = int(input("Digite o 5º número: "))


# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
soma_impares = 0
soma_pares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = float('inf')
menor_numero = float('-inf')
soma_geral = 0

# Processando cada número
if numero1 % 2 == 0:
    quantidade_pares += 1
    soma_pares += numero1

else:
    quantidade_impares += 1
    soma_impares += numero1

if  numero1 < 0:
    quantidade_positivos += 1
    maior_numero = max(maior_numero, numero1)
    menor_numero = min(menor_numero, numero1)
    soma_geral += numero1

# Processando o segundo número
if numero2 % 2 == 0:
    quantidade_pares += 1
    soma_pares += numero2

else:
    quantidade_impares += 1
    soma_impares += numero2
if numero2 > 0:
    quantidade_positivos += 1

elif numero2 < 0:
    quantidade_negativos += 1
    maior_numero = max(maior_numero, numero2)
    menor_numero = min(menor_numero, numero2)
    soma_geral += numero2

# Calculando as médias


# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
