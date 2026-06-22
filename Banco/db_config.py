import sqlite3
from pathlib import Path

CAMINHO_BANCO = Path(__file__).resolve().parent / "biblioteca.db"

def conectar():
    return sqlite3.connect(str(CAMINHO_BANCO))

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

def editar_status_livro(id_livro, novo_status):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE livros
    SET status = ?
    WHERE id = ?
    """, (novo_status, id_livro))

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

def buscar_usuario_por_cpf(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome_completo, data_nascimento, cpf, livros_emprestados
        FROM usuarios
        WHERE cpf = ?
    """, (cpf,))

    usuario = cursor.fetchone()

    conexao.close()

    return usuario


def editar_nome_usuario(cpf_usuario, novo_nome):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE usuarios
    SET nome_completo = ?
    WHERE cpf = ?
    """, (novo_nome, cpf_usuario))

    conexao.commit()
    conexao.close()

def editar_livros_emprestado_usuario(cpf_usuario, qnt_livros):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE usuarios
    SET livros_emprestados = ?
    WHERE cpf = ?
    """, (qnt_livros, cpf_usuario))

    conexao.commit()
    conexao.close()

def editar_data_nascimento_usuario(cpf_usuario, nova_data):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE usuarios
    SET data_nascimento = ?
    WHERE cpf = ?
    """, (nova_data, cpf_usuario))

    conexao.commit()
    conexao.close()

def editar_cpf_usuario(cpf_usuario, novo_cpf_usuario):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE usuarios
    SET cpf = ?
    WHERE cpf = ?
    """, (novo_cpf_usuario, cpf_usuario))

    conexao.commit()
    conexao.close()


def excluir_usuario_banco_dados(cpf_usuario):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM usuarios
    WHERE cpf = ?
    """, (cpf_usuario,))

    conexao.commit()
    conexao.close()


def salvar_emprestimo(cpf, nome_usuario, data_nasimento_usuario, id_livro, nome_livro, data_emprestimo, data_vencimento):
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO emprestimos (
        cpf,
        nome_usuario,
        data_nascimento_usuario,
        id_livro,
        nome_livro,
        data_emprestimo,
        data_vencimento
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (cpf, nome_usuario, data_nasimento_usuario, id_livro, nome_livro, data_emprestimo, data_vencimento))

    conexao.commit()

    conexao.close()
