import os
from dataclasses import dataclass

os.system('cls')

#Definindo uma classe.
@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Telefone: {self.telefone}')

cliente = Cliente(
nome = input('Digite seu nome: '),
email = input('Digite seu email: '),
telefone = input('Digite o seu telefone ')
)

print('\n= Exibindo dados do cliente =')
cliente.mostrar_dados()