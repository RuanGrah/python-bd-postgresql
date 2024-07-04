from cadastro_categoria import menu_categoria
from cadastro_produto import menu_produto
from cadastro_cliente import menu_cliente
from cadastro_usuario import menu_usuario
from vendas import menu_vendas
from conexao import conecta_db


def login(conexao) -> None:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    cursor = conexao.cursor()
    cursor.execute("select id,login,senha,admin from usuario where login = %s and senha = %s", (login,senha))
    registro = cursor.fetchone()

    if registro is None:
        print("Usuario ou senha invalidos")
    else:
        admin = registro[3]
        menu_principal(admin)
        



def menu_principal(admin):
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
             menu_vendas(opcao)
        elif opcao == "5":
             menu_usuario(opcao,admin)
        elif opcao == "6":
            break
        else :
            print ("Opção invalida, tente novamente")


if __name__ == "__main__":
    conexao = conecta_db()
    login(conexao)
    