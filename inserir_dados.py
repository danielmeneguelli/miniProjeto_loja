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
    print(cursor.rowcount, 'registros inseridos na tabela!')
    cursor.close()

except Error as erro:
    print('Falha ao inserir dados no MySQL: {}'.format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada")
