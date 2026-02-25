import os

#limpe o terminal

os.system("cls")
print("- quanridade de produtos")
quantidade = int(input("Digite a quantidade de produtos: "))
nome = input("Digite o nome do produto: ")
valor = 1.30
valor = 1.00

#calcule

if quantidade >= 12:

    soma = (quantidade * 1.30)
    print(f"O valor total é: R${soma: .2f}")

else: quantidade < 12 
valor = 1.00
soma = (quantidade * 1.00)
print(f"O valor total é: R${soma: .2f}")

