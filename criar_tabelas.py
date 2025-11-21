import mysql.connector
try:

    # Conectando no banco para criar as tabelas

    con = mysql.connector.connect(
        host= 'localhost',
        user="root", 
        password='D@ni271203',
        database='loja_db'
    )

    cursor = con.cursor()

    # Criando as tabelas:
    # - Tabela Cliente:

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                email VARCHAR(100),
                idade INT
                )
                """)

    # - Tabela Produtos:

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                preco DECIMAL(10,2),
                estoque INT
                )
                """)

    # - Tabela pedidos:

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pedidos(
                id INT AUTO_INCREMENT PRIMARY KEY,
                cliente_id INT,
                produto_id INT,
                quantidade INT,
                total DECIMAL(10,2),
                FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                FOREIGN KEY (produto_id) REFERENCES produtos(id)
                )
                """)

    con.commit()
    print("Tabelas criadas com sucesso!")
except mysql.connector.Error as erro:
    print("Erro ao criar as tabelas no MySQL: {}".format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print('conexão ao MySQL finalizada!')    

