import os
from dataclasses import dataclass

os.system('cls')

#Definindo uma classe.
@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

print('= Solicitando dados do cliente =')
cliente = Cliente(
nome = input('Digite seu nome: '),
email = input('Digite seu email: '),
telefone = input('Digite o seu telefone ')
)

print('\n= Exibindo dados do cliente =')
print(f'Nome: {cliente.nome}')
print(f'E-mail: {cliente.email}')
print(f'Telefone: {cliente.telefone}')