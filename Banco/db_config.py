import sqlite3

def conectar():
    return sqlite3.connect("Banco/biblioteca.db")

def salvar_livro(nome, descricao, estado_livro, entregue):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO livros (
        nome_livro,
        descricao,
        estado_livro,
        entregue_por
    )
    VALUES (?, ?, ?, ?)
    """, (nome, descricao, estado_livro, entregue))

    conexao.commit()

    conexao.close()


def buscar_livro_nome(nome):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    WHERE nome_livro LIKE ?
    """, (f"%{nome}%",))

    livros = cursor.fetchall()

    conexao.close()

    return livros


def buscar_livro_id(id_livro):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    WHERE id = ?
    """, (id_livro,))

    livro = cursor.fetchone()

    conexao.close()

    return livro

def buscar_todos_livros():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    ORDER BY nome_livro ASC
    """)

    livros = cursor.fetchall()

    conexao.close()

    return livros

def buscar_livros_disponiveis():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    WHERE status = 1
    ORDER BY nome_livro ASC
    """)

    livros = cursor.fetchall()

    conexao.close()

    return livros

def buscar_livros_emprestados():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    WHERE status = 0
    ORDER BY nome_livro ASC
    """)

    livros = cursor.fetchall()

    conexao.close()

    return livros


def editar_nome_livro(id_livro, novo_nome):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE livros
    SET nome_livro = ?
    WHERE id = ?
    """, (novo_nome, id_livro))

    conexao.commit()
    conexao.close()

def editar_descricao_livro(id_livro, novo_descricao):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE livros
    SET descricao = ?
    WHERE id = ?
    """, (novo_descricao, id_livro))

    conexao.commit()
    conexao.close()

def editar_condicao_livro(id_livro, novo_condicao):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE livros
    SET estado_livro = ?
    WHERE id = ?
    """, (novo_condicao, id_livro))

    conexao.commit()
    conexao.close()

def editar_entregue_livro(id_livro, novo_entregue):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE livros
    SET entregue_por = ?
    WHERE id = ?
    """, (novo_entregue, id_livro))

    conexao.commit()
    conexao.close()

def excluir_livro(id_livro):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM livros
    WHERE id = ?
    """, (id_livro,))

    conexao.commit()
    conexao.close()

def buscar_cpf_usuario(cpf):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE cpf = ?
    """, (cpf,))

    cpf_usuario = cursor.fetchone()

    conexao.close()

    return cpf_usuario

def salvar_usuario(nome, data, cpf):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO usuarios (
        nome_completo,
        data_nascimento,
        cpf
    )
    VALUES (?, ?, ?)
    """, (nome, data, cpf))

    conexao.commit()

    conexao.close()