import os 

#limpa o terminal.
os.system("cls")

print("solicitando dados. ")
nome = input("digite seu nome: ")

primeiro_nota = float(input("digite a primeira nota: "))
segundo_nota = float(input("digite a segunda nota: "))

media = (primeiro_nota + segundo_nota) / 2
print(f"A media de {nome} é {media:.2f}")

if media>= 7:
    print("aluno aprovado.")
else:
    print("aluno reprovado.")