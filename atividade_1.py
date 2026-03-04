import os 

#limpar o terminal.
os.system("cls || clear")

# Dados já cadastrados
login_cadastrado = "admin"
senha_cadastrada = "1234"

# Solicita dados ao usuário
login_digitado = input("Digite o login: ")
senha_digitada = input("Digite a senha: ")

# Verificação
if login_digitado == login_cadastrado and senha_digitada == senha_cadastrada:
    print("Bem vindo")

else:
    print("Login ou senha invalidos")