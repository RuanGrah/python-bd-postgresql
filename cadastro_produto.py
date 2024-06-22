from conexao import conecta_db

def consultar(conexao):
    cursor = conexao.cursor()
    cursor.execute("select id,descricao,preco,estoque from produto")
    registros = cursor.fetchall()
    print("|-------------------------------|")
    print("| ID   | Descrição      |Preço  |")
    print("|-------------------------------|")

    for registro in registros:
        print(f"|{+registro[0]}    | {registro[1]}   |{registro[2]}| ")
    print("|-------------------------------|")

def inserir(conexao):
    cursor = conexao.cursor()
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = float(input("Digite a quantida do produto em estoque: "))
    
    sql_insert = "insert into produto (descricao,preco,estoque) values (%s,%s,%s)"
    dados = (descricao, preco, estoque)
    
    cursor.execute(sql_insert, dados)
    conexao.commit() 


def menu_produto(opcao):
    print("|------------------------------|")
    print("|       Menu  ->  Produto      |")
    print("|------------------------------|")
    print("|     1 - Consultar Produto    |")
    print("|     2 - Inserir Produto      |")
    print("|     3 - Alterar Produto      |")
    print("|     4 - Deletar Produto      |")
    print("|     5 - Sair do Sistema      |")
    print("|------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            consultar(conexao)
        elif opcao == "2":
            inserir(conexao)
            print("Produto inserido com sucesso")
        elif opcao == "3":
            print("Não foi implementado")
        elif opcao == "4":
            print("Não foi implementado")
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")