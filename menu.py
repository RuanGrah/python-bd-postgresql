from cadastro_categoria import menu_categoria
from cadastro_produto import menu_produto


if __name__ == "__main__": 
    print("|------------------------------|")
    print("|       Menu  ->  Categoria    |")
    print("|------------------------------|")
    print("|     1 - Categoria            |")
    print("|     2 - Produto              |")
    print("|     3 - Cliente              |")
    print("|     4 - Venda                |")
    print("|     5 - Sair do Sistema      |")
    print("|------------------------------|")

  

    while True :
        opcao = input("Escolha uma Opção: ")

        if opcao == "1":
            menu_categoria(opcao)
        elif opcao == "2":
            menu_produto(opcao)
            print("--Categoria Inserida com sucesso--)")
        elif opcao == "3":
            print("Ainda não foi implementado")
        elif opcao == "4":
             print("Ainda não foi implementado")
        elif opcao == "5":
            break
        else :
            print ("Opção invalida, tente novamente")
        