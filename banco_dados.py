import sqlite3
import os
from contextlib import closing

# Nome do arquivo do banco de dados (fica na mesma pasta do programa)
ARQUIVO_BANCO = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pontuacoes.db')

def conectar():
    conexao = sqlite3.connect(ARQUIVO_BANCO)
    return conexao

def criar_tabela():
    conexao = conectar()
    with closing(conexao) as con:
        with closing(con.cursor()) as cursor:
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS pontuacoes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_aluno TEXT NOT NULL,
            acertos INTEGER NOT NULL,   
            erros INTEGER NOT NULL,
            data_hora TEXT DEFAULT (datetime('now', 'localtime'))
            )
            ''')

            con.commit()

def salvar_pontuacao(nome_aluno, acertos, erros):
    conexao = conectar()

    with closing(conexao) as con:
        with closing(con.cursor()) as cursor:
            cursor.execute('''
            INSERT INTO pontuacoes (nome_aluno, acertos, erros)
            VALUES (?, ?, ?)
            ''', (nome_aluno, acertos, erros))

            con.commit()

def buscar_historico(nome_aluno=None):
    conexao = conectar()

    with closing(conexao) as con:
        with closing(con.cursor()) as cursor:
            if nome_aluno:
                cursor.execute('''
                SELECT nome_aluno, acertos, erros, data_hora
                FROM pontuacoes
                WHERE nome_aluno = ?
                ORDER BY id DESC
                ''', (nome_aluno,))

            else:
                cursor.execute('''
                SELECT nome_aluno, acertos, erros, data_hora
                FROM pontuacoes
                ORDER BY id DESC
                ''')

            resultados = cursor.fetchall()
            return resultados

def buscar_ranking(limite=10):
    conexao = conectar()
    with closing(conexao) as con:
        with closing(con.cursor()) as cursor:
            cursor.execute('''
            SELECT nome_aluno, acertos, erros, data_hora
            FROM pontuacoes
            ORDER BY acertos DESC, erros ASC
            LIMIT ?
            ''', (limite,))

            resultados = cursor.fetchall()
            return resultados