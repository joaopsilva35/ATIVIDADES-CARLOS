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

print('= Solicitando dados do paciente =')
paciente1 = Paciente(
nome= input('Digite seu nome: '),
idade= input('Digite sua idade: '),
peso= input('Digite o seu peso: '),
altura= input('digite a sua altura: ')
)

print('\n= Exibindo dados do paciente =')
print(f'Nome: {paciente1.nome}')
print(f'idade: {paciente1.idade} anos')
print(f'peso: {paciente1.peso} kg')
print(f'altura: {paciente1.altura} m')