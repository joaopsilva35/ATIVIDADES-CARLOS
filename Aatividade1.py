def exibir_menu():
    print("\n= BANCO SENAI DIGITAL =")
    print("1- CRIAR USUÁRIO")
    print("2- SACAR")
    print("3- DEPOSITAR")
    print("4- SALDO")
    print("5- SAIR")
    return input("Escolha uma opção: ")

def criar_usuario(nomes, saldos):
    nome = input("Digite o nome do novo usuário: ")
    nomes.append(nome)
    saldos.append(0.0) 
    print(f"Usuário '{nome}' criado com sucesso!")

def buscar_usuario(nomes):
    nome = input("Digite o nome do usuário: ")
    if nome in nomes:
        return nomes.index(nome) 
    else:
        print("Erro: Usuário não encontrado.")
        return -1

def sacar(nomes, saldos):
    indice = buscar_usuario(nomes)
    if indice != -1:
        valor = float(input("Digite o valor para saque: R$ "))
        if valor > 0 and valor <= saldos[indice]:
            saldos[indice] -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        elif valor > saldos[indice]:
            print("Erro: Saldo insuficiente.")
        else:
            print("Erro: Valor inválido.")

def depositar(nomes, saldos):
    indice = buscar_usuario(nomes)
    if indice != -1:
        valor = float(input("Digite o valor para depósito: R$ "))
        if valor > 0:
            saldos[indice] += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Erro: Valor inválido.")

def ver_saldo(nomes, saldos):
    indice = buscar_usuario(nomes)
    if indice != -1:
        print(f"Saldo atual de {nomes[indice]}: R$ {saldos[indice]:.2f}")

def main():
    vetor_nomes = []
    vetor_saldos = []
    
    while True:
        opcao = exibir_menu()
        
        if opcao == '1':
            criar_usuario(vetor_nomes, vetor_saldos)
        elif opcao == '2':
            sacar(vetor_nomes, vetor_saldos)
        elif opcao == '3':
            depositar(vetor_nomes, vetor_saldos)
        elif opcao == '4':
            ver_saldo(vetor_nomes, vetor_saldos)
        elif opcao == '5':
            print("Encerrando o sistema do Banco SENAI Digital. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()