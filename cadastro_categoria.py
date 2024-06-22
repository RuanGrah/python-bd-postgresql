from conexao import conecta_db


def consultar(conexao):
    cursor = conexao.cursor()
    cursor.execute("select id,nome from categoria")
    registros = cursor.fetchall()
    for registro in registros:
        print(f"| ID ..:  {+registro[0]}  Nome ..: {registro[1]}")
        print("|-------------------------------|")

def inserir(conexao):
    cursor = conexao.cursor()
    nome_categoria = input("Digite o nome da categoria: ")
    sql_insert = "insert into categoria (nome) values ('"+ nome_categoria + "')"
    cursor.execute(sql_insert)
    conexao.commit() 

def alterar(conexao):
    cursor = conexao.cursor()
    id = input("Informe o ID: ")
    nome_categoria = input("Digite o nome da categoria: ")
    sql_update = "update categoria set nome ='" + nome_categoria + "' where id = " + id + ""
    cursor.execute(sql_update)
    conexao.commit()

def deletar(conexao):
    cursor = conexao.cursor()
    id = input("Informe o ID: ")
    nome_categoria = input("Digite o nome da categoria: ")
    sql_update = "delete from categoria where id = " + id 
    cursor.execute(sql_update)
    conexao.commit()


def menu_categoria(opcao):
    print("|------------------------------|")
    print("|       Menu  ->  Categoria    |")
    print("|------------------------------|")
    print("|     1 - Consultar Categoria  |")
    print("|     2 - Inserir Categoria    |")
    print("|     3 - Alterar Categoria    |")
    print("|     4 - Deletar Categoria    |")
    print("|     5 - Sair do Sistema      |")
    print("|------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")
        if opcao == "1":    
            consultar(opcao)
        elif opcao == "2":
            inserir(opcao)
        elif opcao == "3":
            alterar(opcao)
        elif opcao == "4":
            deletar(opcao)
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")