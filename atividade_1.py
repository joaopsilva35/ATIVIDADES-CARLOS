import os 

#limpa o terminal.
os.system("cls")

print("solicitando dados. ")
nome = input("digite seu nome: ")


primeiro_nota = float(input("digite a primeira nota: "))
segundo_nota = float(input("digite a segunda nota: "))
terceira_nota = float(input("digite a terceira nota: "))
perguntar = input("Deseja adicionar mais uma nota 'Sim' para adicionar ou 'Nao' para nao adicionar: ")
quarta_nota = float(input("Digite a quarta nota: "))


media = (primeiro_nota + segundo_nota + terceira_nota + quarta_nota) / 4
print(f"A media de {nome} é {media:.2f}")
perguntar = input("Deseja adicionar mais uma nota 'Sim' para adicionar ou 'Nao' para nao adicionar: ").upper()


if media>= 7:
    print("aluno aprovado.")
else:
    print("aluno reprovado.")