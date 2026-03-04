import os
os.system("cls")

print("- solicitand dados -")
ano_nacimento = int(input("digite seu nacimento: "))
sexo = input("digite seu sexo: ")

idade = 2026 - ano_nacimento

idade_obrigatorio = idade >= 18
sexo_obrigatorio = sexo == "masculino"

if idade_obrigatorio and sexo_obrigatorio: 
    print("deve apressentar-se ao servico militar obrigatorio")
else:
    print("nao e necessario apresentar-se ao servico militar obrigatorio")
