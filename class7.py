import os
from dataclasses import dataclass

os.system('cls')

#Definindo uma classe.
@dataclass
class Paciente:
    nome: str
    idade: str
    peso: str
    altura: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'idade: {self.idade} anos')
        print(f'peso: {self.peso} kg')
        print(f'altura: {self.altura} m')

print('= Solicitando dados do paciente =')
paciente1 = Paciente(
nome= input('Digite seu nome: '),
idade= input('Digite sua idade: '),
peso= input('Digite o seu peso: '),
altura= input('digite a sua altura: ')
)

print('\n= Exibindo dados do paciente =')