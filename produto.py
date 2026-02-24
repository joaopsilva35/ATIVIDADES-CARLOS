import os 

#limpa o terminal.
os.system("cls")

print("- solicitando dados -")
primeiro_numero = int(input("digite o primeiro numero: "))
segundo_numero = int(input("digite o segundo numero: "))

#calculando.
produto = primeiro_numero + segundo_numero
soma = primeiro_numero + segundo_numero
media = soma / 2 

if primeiro_numero > segundo_numero: 
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero

print("\n- Exibindo dados -")
print(f"soma: {soma}")
print(f"media: {media}")
print(f"produto: {produto}")
print(f"maior numero: {maior}")
print(f"menor numero: {menor}")