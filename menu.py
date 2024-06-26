from cadastro_categoria import menu_categoria
from cadastro_produto import menu_produto
from cadastro_cliente import menu_cliente
from cadastro_usurario import menu_usuario
from conexao import conecta_db


def login(conexao) -> None:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    cursor = conexao.cursor()
    cursor.execute("select id,login,senha from usuario where login = %s and senha = %s", (login,senha))
    registros = cursor.fetchone()

    if registros is None:
        print("Usuario ou senha invalidos")
    else:
        menu_principal()
        



def menu_principal():
    print("|------------------------------|")
    print("|       Menu  ->  Categoria    |")
    print("|------------------------------|")
    print("|     1 - Categoria            |")
    print("|     2 - Produto              |")
    print("|     3 - Cliente              |")
    print("|     4 - Venda                |")
    print("|     5 - Usuario              |")
    print("|     6 - Sair do Sistema      |")
    print("|------------------------------|")

  

    while True :
        opcao = input("Escolha uma Opção: ")

        if opcao == "1":
            menu_categoria(opcao)
        elif opcao == "2":
            menu_produto(opcao)
        elif opcao == "3":
            menu_cliente(opcao)
        elif opcao == "4":
             print("Ainda não foi implementado")
        elif opcao == "5":
             menu_usuario(opcao)
        elif opcao == "6":
            break
        else :
            print ("Opção invalida, tente novamente")


if __name__ == "__main__":
    conexao = conecta_db()
    login(conexao)
    