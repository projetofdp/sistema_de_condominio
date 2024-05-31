import sqlite3
from datetime import datetime


def criar_banco_de_dados():
    conn = sqlite3.connect('encomendas.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS encomendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        porteiro TEXT NOT NULL,
        destinatario TEXT NOT NULL,
        apartamento TEXT NOT NULL,
        data_hora_entrega TEXT NOT NULL,
        nome_retirada TEXT,
        documento_retirada TEXT,
        data_hora_retirada TEXT 
    )
    ''')

    conn.commit()
    conn.close()


def adicionar_encomenda(porteiro, destinatario, apartamento):
    data_hora_entrega = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('encomendas.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO encomendas (porteiro, destinatario, apartamento, data_hora_entrega)
    VALUES (?, ?, ?, ?)
    ''', (porteiro, destinatario, apartamento, data_hora_entrega))

    conn.commit()
    conn.close()


def buscar_encomenda(id_encomenda, nome_retirada, documento_retirada):
    data_hora_retirada = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('encomendas.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE encomendas
    SET nome_retirada = ?, documento_retirada = ?, data_hora_retirada = ?
    WHERE id = ?
    ''', (nome_retirada, documento_retirada, data_hora_retirada, id_encomenda))

    conn.commit()
    conn.close()


def listar_encomendas():
    conn = sqlite3.connect('encomendas.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM encomendas')
    encomendas = cursor.fetchall()

    conn.close()
    return encomendas
