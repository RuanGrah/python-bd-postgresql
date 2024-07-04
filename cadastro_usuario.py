from conexao import conecta_db 

def consultar(conexao):
    cursor = conexao.cursor()
    cursor.execute("select id,login from usuario")
    registros = cursor.fetchall()
    for registro in registros:
        print(f"| ID ..:  {+registro[0]}  Usuario ..: {registro[1]}")
        print("|-------------------------------|")

def inserir(conexao):
    cursor = conexao.cursor()
    print("Cadastro de Usuario")
    login_usuario = input("Crie um login: ")
    senha_usuario = input("Crie uma senha: ")
    verificacao = input("Admin? (Sim ou Não): ")

    if verificacao == "Sim":
        admin = "S"  
    else:
        admin = "N"


    sql_insert = "insert into usuario (login, senha, admin ) values ('" + login_usuario + "','" + senha_usuario + "', '" + admin + "')"
    
    cursor.execute(sql_insert)
    conexao.commit() 

def update(conexao):
    cursor = conexao.cursor()
    print("Alteração de Usuario ")
    login_usuario = input("Informe o seu login: ")                                                                                 
    nova_senha = input("Informe sua nova senha")
    sql_update = "update usuario set senha ='" + nova_senha + "' where login = " + login_usuario + ""
    cursor.execute(sql_update)
    conexao.commit()

def delete(conexao):
    cursor = conexao.cursor()
    id = input("Informe o ID: ")
    sql_update = "delete from usuario where id = " + id 
    cursor.execute(sql_update)
    conexao.commit()

def menu_usuario_admin(opcao):
    print("|------------------------------|")
    print("|       Menu  ->  Usuario      |")
    print("|------------------------------|")
    print("|     1 - Consultar Usuario    |")
    print("|     2 - Inserir Usuario      |")
    print("|     3 - Alterar Usuario      |")
    print("|     4 - Deletar Usuario      |")
    print("|     5 - Sair do Sistema      |")
    print("|------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            consultar(conexao)
        elif opcao == "2":
            inserir(conexao)
            print("Usuario inserido com sucesso")
        elif opcao == "3":
            update(conexao)
            print("Update feito com sucesso")
        elif opcao == "4":
            delete(conexao)
            print("Usuario deletado com sucesso")
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")


def menu_usuario_not_admin(opcao):
    print("|------------------------------|")
    print("|       Menu  ->  Usuario      |")
    print("|------------------------------|")
    print("|     1 - Alterar Usuario      |")
    print("|     2 - Sair do Sistema      |")
    print("|------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            update(conexao)
            print("Update feito com sucesso")
        elif opcao == "2":
            break
        else:
            print("Opção invalida, tente novamente")


def menu_usuario(opcao,admin):
    if admin == "S":
        menu_usuario_admin(opcao)
    else: 
        menu_usuario_not_admin(opcao)    