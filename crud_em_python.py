import mysql.connector

#CONECTANDO AO BANCO DE DADOS E FAZENDO AS CONFIGURAÇÕES INCIAIS

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'admin',
    password = 'admin',
    database = 'bd_aula'
)

cursor = conexao.cursor()

#CREATE, INSERINDO DADOS NA TABELA
#nome = 'Chocolate'
#valor = '15'
#comando = f"INSERT INTO vendas (nome_produto, valor) VALUES ('{nome}', '{valor}')"
#cursor.execute(comando)
#conexao.commit() #Comando usado todas as vezes em que há edição no banco de dados


#READ, lendo dados das tabelas

comando = 'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() #Faz a leitura dos dados do banco e traz para o código
print(resultado)


#UPDATE
valor = '7'
nome = 'Farinha'
comando = f"UPDATE vendas SET valor = '{valor}' WHERE nome_produto = '{nome}'"
cursor.execute(comando)
conexao.commit()


#DELETE
comando = f"DELETE FROM vendas WHERE nome_produto = 'Chocolate'"
cursor.execute(comando)
conexao.commit()


#DESLIGANDO A CONEXÃO COM O BANCO
cursor.close()
conexao.close()