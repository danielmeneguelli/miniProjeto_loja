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
    
    cursor = con.cursor()
    cursor.execute(inserir_clientes)
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
