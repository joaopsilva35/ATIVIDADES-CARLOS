import os 

os.system("cls") #Limpa o terminal. 

pares = 0 
impares = 0 
soma_geral = 0 
soma_pares = 0 
contador_geral = 0 

while True:
    numero = int(input("Digite um numero: "))
    if numero > 0: 
        contator_geral  += 1 
        soma_geral += numero 
        if numero % 2 == 0: 
            pares += 1 
            soma_pares += 1 
        else:
            impares += 1 
    if numero == 0: 
        break 

media_pares = soma_pares / pares 
media_geral = soma_geral / contador_geral 

print(f"\nQuantidade de pares: {pares}")
print(f"Quantidades de impares: {impares}")
print(f"media de numeros pares: {media_pares}")
print(f"media geral: {media_geral}")