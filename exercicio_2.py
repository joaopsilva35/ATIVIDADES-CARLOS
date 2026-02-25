import os

#limpa o terminal
os.system("cls")

print("solicitando dados. ")
idade = int(input("digite sua idade: "))



if idade < 16:
    print("voce nao pode votar")
elif idade == 16 or idade == 17:
    print("voce nao pode votar (nao obrigatorio).")
elif idade >= 18 and idade <= 65:
    print("voce e obrigado a votar.")
elif idade > 65:
    print("voce nao e obrigado a votar")
