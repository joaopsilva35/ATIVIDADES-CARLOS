import os
from dataclasses import dataclass

os.system('cls')

#Definindo uma classe.
@dataclass
class funcionario:
    nome: str
    matricula: int
    email: str
    setor: str

Funcionario1 = funcionario("pedro", "pedro@gmail.com", "0800", "Tecnico")


print(f'Nome: {Funcionario1.nome}')
print(f'E-mail: {Funcionario1.email}')
print(f'matricula: {Funcionario1.matricula}')
print(f'setor: {Funcionario1.setor}')