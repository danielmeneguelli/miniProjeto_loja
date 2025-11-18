import mysql.connector

con = mysql.connector.connect(host= "localhost",
                              user= "root", 
                              password= "D@ni271203")

cursor = con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS loja_db")

print("banco criado com sucesso!")

