import os

os.system("cls")

# Variáveis para armazenar os números
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))
n4 = int(input("Digite o 4º número: "))
n5 = int(input("Digite o 5º número: "))


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
if n1 % 1 == 0:
    quantidade_pares += 1
    soma_pares += n1

else:
    quantidade_impares += 1
    soma_impares += n1

if  n1 < 1:
    quantidade_positivos += 1
    maior_numero = max(maior_numero, n1)
    menor_numero = min(menor_numero, n1)
    soma_geral += n1

# Processando o segundo número
if n2 % 2 == 0:
    quantidade_pares += 2
    soma_pares += n2

else:
    quantidade_impares += 1
    soma_impares += n2
if n2 > 0:
    quantidade_positivos += 1

elif n2 < 0:
    quantidade_negativos += 1
    maior_numero = max(maior_numero, n2)
    menor_numero = min(menor_numero, nu2)
    soma_geral += n2

# Calculando as médias


# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
