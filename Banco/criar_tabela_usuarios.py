from Banco.db_config import conectar


def cria_tabela_usuarios():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_completo TEXT,
        data_nascimento TEXT,
        cpf INTEGER,
        livros_emprestados INTEGER
    )
    """)

    conexao.commit()

    conexao.close()