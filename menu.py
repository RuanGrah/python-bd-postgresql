from cadastro_categoria import alterar, consultar, deletar, inserir, menu_categoria
from conexao import conecta_db



if __name__ == "__main__": 
    print("|------------------------------|")
    print("|       Menu  ->  Categoria    |")
    print("|------------------------------|")
    print("|     1 - Categoria            |")
    print("|     2 - Inserir Categoria    |")
    print("|     3 - Alterar Categoria    |")
    print("|     4 - Deletar Categoria    |")
    print("|     5 - Sair do Sistema      |")
    print("|------------------------------|")

    conexao = conecta_db()

    while True :
        opcao = input("Escolha uma Opção: ")

        if opcao == "1":
            menu_categoria(opcao)
        elif opcao == "2":
            inserir(conexao)
            print("--Categoria Inserida com sucesso--)")
        elif opcao == "3":
            alterar(conexao)
            print("--Alteração feita com sucesso--")
        elif opcao == "4":
            deletar(conexao)
            print("--Categoria deletada com sucesso--")
        elif opcao == "5":
            break
        else :
            print ("Opção invalida, tente novamente")
        