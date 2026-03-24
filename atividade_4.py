import os 

os.system("cls") #Limpar o terminal. 

soma_salario = 0
contador_pessoas = 0 
maoir_idade = 0 
menor_idade = 0 
mulheres_salarios5k = 0 

opcao = 0 

while True:
    print("""
--- MENU DE PESQUISA --- 
1  -  Adicionar pessoa
2  -  Exibir resultado 
3  -  Sair
""")
    
opcao = int(input("Digite a opcao desejada: "))

match opcao:
    case 1:
        print("-- CADASTRO --")
        idade = int(input("Digite a sua idade: "))
        sexo = int(input("Figite o seu sexo: "))
        salario = int(input("digite o seu salario"))

        soma_salario = max(idade, maoir_idade)
        menor_idade = min(idade, menor_idade)

        if sexo == "F" and salario >= 5000:
            mulheres_salarios5k += 1 

            print("Pessoa adicionada com sucesso. \n")
        
    case 2:
        if contador_pessoas == 0:
            print("\nNunhum pessoa cadastradas ainda. \n")
        else:
            media_salario = soma_salario / contador_pessoas
            