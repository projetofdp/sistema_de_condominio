import sqlite3

# criando conexão
try:
    con = sqlite3.connect('cadastro_encomendas.db')
    print('Conexão com o banco de dados realizado com sucesso!')
except sqlite3.Error as e:
    print('Erro ao conectar com o banco de dados:', e)

# criando tabela
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS encomendas(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        porteiro TEXT,
        destinatario TEXT,
        apartamento TEXT,
        data_hora_entrega TEXT,
        nome_retirada TEXT,
        documento_retirada TEXT,
        data_hora_retirada TEXT
        )""")

        print("Tabela Encomendas criado com sucesso")

except sqlite3.Error as e:
    print('Erro ao criar a tabela de encomendas:', e)
    