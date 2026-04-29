import os
from dataclasses import dataclass

os.system('cls')

#Definindo uma classe.
@dataclass
class Endereco:
    logradouro: str
    numero: str

@dataclass
class Cliente:
    nome: str
    idade: int
    endereco: Endereco

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'endereco: {self.endereco.logradouro}')
        print(f'Numero: {self.endereco.numero}')
    
print('= solicintando dados do cliente')
cliente = Cliente(
    nome= input('Digite seu nome: '),
    idade= int(input('Digite sua idade: ')),
    endereco= Endereco(
        logradouro= input('digite o seu endereco: '),
        numero= input('digite seu numero: ')
        )
)

print('\n= Exibindo dados do cliente =')
cliente.mostrar_dados()