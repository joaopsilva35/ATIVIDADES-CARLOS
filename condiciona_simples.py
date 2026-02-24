import os 

#limpar o terminal.
os.system("cls || clear")

idade = int(input("digite sua idade "))

if idade < 18:
    print("acesso negado.")

    print("programa encerrado.")