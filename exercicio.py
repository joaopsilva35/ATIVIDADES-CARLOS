import os 

#limpa o terminal.
os.system("cls")

print("- solicitando dados -")
numero_1= int(input("digite um numero inteiro: "))
numero_2 = int(input("digite mais numero inteiro: "))


#calculando. 
produto = numero_1 + numero_2
soma = numero_1 + numero_2 
media = soma / 2
numero_igual = numero_1 + numero_2

if numero_1 > 0:
    maior_numero = numero_1
    menor_numero = numero_2
    igual = numero_1
else:
    maior_numero = numero_2
    menor_numero = numero_1
    igual = numero_2

print("\n- Exibindo dados -")
print(f"soma: {soma}")
print(f"media: {media}")
print(f"produto: {produto}")
print(f"maior numero: {maior_numero}")
print(f"menor numero: {menor_numero}")
print(f"numero igual: {igual}")


