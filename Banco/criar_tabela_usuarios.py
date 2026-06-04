from Banco.db_config import conectar


def cria_tabela_usuarios():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_completo TEXT,
        data_nascimento TEXT,
        cpf TEXT,
        livros_emprestados INTEGER DEFAULT 0
    )
    """)

    conexao.commit()

    conexao.close()