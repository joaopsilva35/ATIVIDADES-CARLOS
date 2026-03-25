import os 

os.system("cls")

#Criando um vetor.
vetor_notas = []
QUANTIDADE_NOTAS = 3

print("Adicionando 3 notas.")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite A{i+1}ª nota: "))
    vetor_notas.append(nota)

media = sum(vetor_notas) / QUANTIDADE_NOTAS

print("\nExibindo as notas informadas.")
for uma_nota in vetor_notas:
    print(f"Nota: {uma_nota}")
    