import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Pessoa:
    nome: str
    idade: int


@dataclass
class Pet:
    nome: str
    idade: int

#Usando uma classe.
pessoa1 = Pessoa('Marta', 20)
pessoa2 = Pessoa('Marta', 20)

pet1 = Pet('Totó', 4)
pet2 = Pet('Totó', 4)

print(f"Nome: {pessoa1.nome} \n idade: {pessoa1.idade}\n")
print(f"Nome: {pessoa2.nome} \n idade: {pessoa2.idade}\n")

print(f"Nome: {pet1.nome} \n idade: {pet1.idade}\n")
print(f"Nome: {pet2.nome} \n idade: {pet2.idade}\n")