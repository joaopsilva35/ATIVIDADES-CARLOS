import os 

#limpar o terminal.
os.system("cls || clear")

numero= int(input("digite seu numero: "))

#condicional composta.
if numero < 10:
    print("numero é menor que 10.")
else:
    print("numero é maior que 10")

print("programa encerrado.")