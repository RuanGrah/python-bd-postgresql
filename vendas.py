from conexao import conecta_db 
from datetime import datetime

def insert_venda(conexao, venda, total_venda):
    cursor = conexao.cursor()
    sql_insert = """
        insert into venda (cliente_id,numero_venda,data_venda,valor_venda)
        values (%s, %s, %s, %s) RETURNING id;
        """
    dados = (venda[0],venda[1],venda[2],total_venda)
    cursor.execute(sql_insert, dados)
    ''
    venda_id = cursor.fetchone()[0]
    conexao.commit()
    return venda_id 

def insert_item_venda(conexao, item_venda):
    cursor = conexao.cursor()
    sql_insert = """
        insert into itens_venda (venda_id,produto_id,qtde,valor_unitario,valor_total)
        values (%s, %s, %s, %s,%s);
        """
    cursor.execute(sql_insert, item_venda)
    conexao.commit() 

def calcular_total_venda(itens_venda):
    total_venda = 0 
    for item in itens_venda:
        total_venda = total_venda + item['valor_total']
    return total_venda



def consultar(conexao):
    
    cursor = conexao.cursor()
    cursor.execute("select id,login from usuario")
    registros = cursor.fetchall()
    for registro in registros:
        print(f"| ID ..:  {+registro[0]}  Cliente ..: {registro[1]}")
        print("|-------------------------------|")

  
    print("Consultar")

def criar_venda(conexao):
    venda = alimentar_venda()
    itens_venda = alimentar_itens()

    try:

        total_venda = calcular_total_venda(itens_venda)
        venda_id = insert_venda(conexao, venda, total_venda)
        
        for item in itens_venda: 
            item_data = (venda_id, item['produto_id'], item['quantidade'], item['preco_unitario'], item['valor_total'])

            insert_item_venda(conexao, item_data)

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao inserir vendas e itens: {e}")
    finally:
        conexao.close()
        

def alimentar_venda():
    
    id_cliente = int(input("Digite o id do cliente: "))
    numero_venda = 0
    data_atual = datetime.now()
    data_venda = data_atual
    valor_venda = 0 #Calcular o total dos itens
    return(id_cliente, numero_venda, data_venda, valor_venda)

def alimentar_itens():
    itens_venda = []
    while (True):
        produto_id = int(input("Digite o id do produto : "))
        quantidade = int(input("Digite a quantidade : "))
        preco_unitario = float(input("Digite o preço unitario : "))
        valor_total = quantidade * preco_unitario
        itens_venda.append({"produto_id": produto_id, "quantidade": quantidade, "preco_unitario": preco_unitario, "valor_total": valor_total})

        continuar = input("Deseja adicionar outro item? (S/N): ")

        if continuar != "S":
            break
    return itens_venda

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
        elif opcao == "2":
            criar_venda(conexao)
        elif opcao == "3":
            break
        else:
            print("Opção invalida, tente novamente")