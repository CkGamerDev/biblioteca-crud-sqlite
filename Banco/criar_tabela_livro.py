from Banco.db_config import conectar


def cria_tabela_livros():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_livro TEXT,
        descricao TEXT,
        estado_livro TEXT,
        entregue_por TEXT,
        status INTEGER DEFAULT 1
    )
    """)

    conexao.commit()

    conexao.close()