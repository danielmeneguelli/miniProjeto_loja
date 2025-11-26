import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost', database='loja_db',user='root', password='D@ni271203')

    inserir_clientes = """INSERT INTO clientes
                        (nome, email, idade)
                        VALUES
                        ('Daniel Campos', 'danielsouza@gmail.com', 23 ),
                        ('Jose Junior', 'josejunior@gmail.com', 32),
                        ('Julia almeida', 'juliaalmeida@gmail.com', 56)
                       """
    
    inserir_produtos = """INSERT INTO produtos 
                        (nome, preco, estoque)
                        VALUES
                        ('carregador', 50, 100),
                        ('monitor', 899.99, 15), 
                        ('mouse', 149.90, 25)
                       """
    
    inserir_pedidos = """INSERT INTO pedidos
                        (cliente_id, produto_id, quantidade, total)
                        VALUES
                        (1, 2, 1, 899.99),
                        (3, 3, 2, 299.80), 
                        (2, 1, 5, 250)
                      """
    cursor = con.cursor()
    cursor.execute(inserir_clientes)
    cursor.execute(inserir_produtos)
    cursor.execute(inserir_pedidos)
    con.commit()
    
    #inserindo dados fornecidos pelo usuário
    
    print('Cadastro de cliente no banco de dados')
    print('Entre com os dados conforme solicitado \n')
    nome = input('Nome do cliente: ')
    email = input('Email: ')
    idade = int(input('Idade: '))

    sql_usuario = "INSERT INTO clientes (nome, email, idade) VALUES (%s, %s, %s)"
    valores = (nome, email, idade)

    cursor.execute(sql_usuario, valores)
    con.commit()

    print(cursor.rowcount, 'registros inseridos na tabela!')
    cursor.close()

except Error as erro:
    print('Falha ao inserir dados no MySQL: {}'.format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada")
