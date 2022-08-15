import mysql

#CONECTANDO AO BANCO DE DADOS E FAZENDO AS CONFIGURAÇÕES INCIAIS

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'admin',
    password = 'admin',
    database = 'bd_aula'
)

cursor = conexao.cursor()
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ()'

# CREATE


cursor.close()
conexao.close()