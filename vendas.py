from conexao import conecta_db 
def consultar(conexao):
    print("Consultar")

def inserir(conexao):
    print("Inserir")


def menu_vendas(opcao):
    print("|------------------------------|")
    print("|       Menu  ->  Vendas       |")
    print("|------------------------------|")
    print("|     1 - Consultar Vendas     |")
    print("|     2 - Inserir Vendas       |")
    print("|     3 - Sair do Sistema      |")
    print("|------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            consultar(conexao)
            print("Update feito com sucesso")
        elif opcao == "2":
            inserir(conexao)
        elif opcao == "3":
            break
        else:
            print("Opção invalida, tente novamente")