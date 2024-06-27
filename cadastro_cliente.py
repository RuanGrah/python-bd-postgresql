from conexao import conecta_db

def consultar(conexao):
    cursor = conexao.cursor()
    cursor.execute("select id, nome, telefone, cidade from cliente")
    registros = cursor.fetchall()
    print("|---------------------------------------------------------------------|")
    print("| ID   | Nome             |Telefone               |Cidade             |")
    print("|---------------------------------------------------------------------|")

    for registro in registros:
        print(f"|{+registro[0]}    | {registro[1]}   |{registro[2]}| {registro[3]}|")
    print("|---------------------------------------------------------------------|")

def inserir(conexao):
    cursor = conexao.cursor()
    nome_cliente = input("Digite o nome do cliente: ")
    telefone = str(input("Digite o telefone do cliente: "))
    cidade = (input("Digite a cidade do cliente: "))

    sql_insert = "insert into cliente (nome,telefone,cidade) values ('" + nome_cliente + "','" + telefone + "','" + cidade + "')"
    
    cursor.execute(sql_insert)
    conexao.commit() 

def update (conexao):
    cursor = conexao.cursor()
    id = input("Informe o ID: ")
    nome_cliente = input("Informe o nome do cliente: ")
    telefone = input("Informe o telefone do cliente: ")
    cidade = input("Informe a cidade do cliente: ")

    sql_update = "update cliente set nome = '" + nome_cliente + "', telefone = '" + telefone + "', cidade = '" + cidade + "' where id = " + id + ""
    dados = (id, nome_cliente, telefone, cidade)
    cursor.execute(sql_update, dados)
    conexao.commit()
    
def delete(conexao):
    cursor = conexao.cursor()
    id = input("Informe o ID: ")
    sql_update = "delete from cliente where id = " + id 
    cursor.execute(sql_update)
    conexao.commit()

def menu_cliente(opcao):
    print("|------------------------------|")
    print("|       Menu  ->  Categoria    |")
    print("|------------------------------|")
    print("|     1 - Consultar Clientes   |")
    print("|     2 - Inserir Cliente      |")
    print("|     3 - Alterar Cliente      |")
    print("|     4 - Deletar Cliente      |")
    print("|     5 - Sair do Sistema      |")
    print("|------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")
        if opcao == "1":    
            consultar(conexao)
        elif opcao == "2":
            inserir(conexao)
        elif opcao == "3":
            update(conexao)
        elif opcao == "4":
            delete(conexao)
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")