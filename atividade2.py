import os 

os.system("cls")

def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

print("= Solicitando da dados =")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Chamando a função para calcular a média
media = calcular_media(nota1, nota2)

print("= Exibindo resultado =")
print(f"Média: {media}") 