from Banco.db_config import conectar


def cria_tabela_emprestimo():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emprestimos (
        cpf TEXT,
        nome_usuario TEXT,
        data_nascimento_usuario TEXT,
        id_livro INTEGER,
        nome_livro TEXT,
        data_emprestimo TEXT,
        data_vencimento TEXT
    )
    """)

    conexao.commit()

    conexao.close()