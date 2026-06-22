import sqlite3
from datetime import date

from flask import Flask, flash, redirect, render_template, request, url_for

from Banco.criar_tabela_emprestimo import cria_tabela_emprestimo
from Banco.criar_tabela_livro import cria_tabela_livros
from Banco.criar_tabela_usuarios import cria_tabela_usuarios
from Banco.db_config import (
    buscar_cpf_usuario,
    buscar_livro_id,
    buscar_usuario_por_cpf,
    conectar,
    editar_livros_emprestado_usuario,
    editar_status_livro,
    excluir_livro,
    excluir_usuario_banco_dados,
    salvar_emprestimo,
    salvar_livro,
    salvar_usuario,
)
from Validacoes.validar_cpf import validar_cpf

app = Flask(__name__)
app.secret_key = "bibiotleca-flask"


def preparar_banco():
    cria_tabela_livros()
    cria_tabela_usuarios()
    cria_tabela_emprestimo()


def limpar_cpf(cpf):
    return "".join(filter(str.isdigit, cpf or ""))


def consultar(sql, parametros=(), unico=False):
    conexao = conectar()
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    resultado = cursor.fetchone() if unico else cursor.fetchall()
    conexao.close()
    return resultado


def executar(sql, parametros=()):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    conexao.commit()
    conexao.close()


def contar(sql, parametros=()):
    linha = consultar(sql, parametros, unico=True)
    return linha[0] if linha else 0


@app.context_processor
def utilidades_templates():
    return {
        "rotulo_status_livro": lambda status: "Disponivel" if status == 1 else "Emprestado",
        "classe_status_livro": lambda status: "ok" if status == 1 else "alerta",
    }


@app.route("/")
def index():
    estatisticas = {
        "livros": contar("SELECT COUNT(*) FROM livros"),
        "disponiveis": contar("SELECT COUNT(*) FROM livros WHERE status = 1"),
        "emprestados": contar("SELECT COUNT(*) FROM livros WHERE status = 0"),
        "usuarios": contar("SELECT COUNT(*) FROM usuarios"),
    }
    ultimos_livros = consultar("SELECT * FROM livros ORDER BY id DESC LIMIT 5")
    emprestimos = consultar("SELECT rowid, * FROM emprestimos ORDER BY data_vencimento ASC LIMIT 5")

    return render_template(
        "index.html",
        estatisticas=estatisticas,
        ultimos_livros=ultimos_livros,
        emprestimos=emprestimos,
    )


@app.route("/favicon.ico")
def favicon():
    return "", 204


@app.route("/livros", methods=["GET", "POST"])
def livros():
    if request.method == "POST":
        nome = request.form.get("nome_livro", "").strip()
        descricao = request.form.get("descricao", "").strip() or "Sem descricao"
        estado_livro = request.form.get("estado_livro", "").strip() or "Nao definido"
        entregue_por = request.form.get("entregue_por", "").strip()

        if not nome or not entregue_por:
            flash("Preencha o nome do livro e quem entregou.", "erro")
            return redirect(url_for("livros"))

        salvar_livro(nome.upper(), descricao, estado_livro.upper(), entregue_por.upper())
        flash("Livro cadastrado com sucesso.", "sucesso")
        return redirect(url_for("livros"))

    busca = request.args.get("busca", "").strip()
    filtro = request.args.get("status", "todos")
    parametros = []
    sql = "SELECT * FROM livros WHERE 1 = 1"

    if busca:
        sql += " AND (nome_livro LIKE ? OR descricao LIKE ? OR entregue_por LIKE ?)"
        termo = f"%{busca}%"
        parametros.extend([termo, termo, termo])

    if filtro == "disponiveis":
        sql += " AND status = 1"
    elif filtro == "emprestados":
        sql += " AND status = 0"

    sql += " ORDER BY nome_livro ASC"
    lista_livros = consultar(sql, parametros)

    return render_template("livros.html", livros=lista_livros, busca=busca, filtro=filtro)


@app.route("/livros/<int:id_livro>/editar", methods=["GET", "POST"])
def editar_livro(id_livro):
    livro = consultar("SELECT * FROM livros WHERE id = ?", (id_livro,), unico=True)
    if not livro:
        flash("Livro nao encontrado.", "erro")
        return redirect(url_for("livros"))

    if request.method == "POST":
        nome = request.form.get("nome_livro", "").strip()
        descricao = request.form.get("descricao", "").strip() or "Sem descricao"
        estado_livro = request.form.get("estado_livro", "").strip() or "Nao definido"
        entregue_por = request.form.get("entregue_por", "").strip()
        status = int(request.form.get("status", livro["status"]))

        if not nome or not entregue_por:
            flash("Preencha o nome do livro e quem entregou.", "erro")
            return redirect(url_for("editar_livro", id_livro=id_livro))

        executar(
            """
            UPDATE livros
            SET nome_livro = ?, descricao = ?, estado_livro = ?, entregue_por = ?, status = ?
            WHERE id = ?
            """,
            (nome.upper(), descricao, estado_livro.upper(), entregue_por.upper(), status, id_livro),
        )
        flash("Livro atualizado com sucesso.", "sucesso")
        return redirect(url_for("livros"))

    return render_template("editar_livro.html", livro=livro)


@app.route("/livros/<int:id_livro>/excluir", methods=["POST"])
def excluir_livro_web(id_livro):
    livro = buscar_livro_id(id_livro)
    if not livro:
        flash("Livro nao encontrado.", "erro")
    elif livro[5] == 0:
        flash("Nao e possivel excluir um livro emprestado.", "erro")
    else:
        excluir_livro(id_livro)
        flash("Livro excluido com sucesso.", "sucesso")
    return redirect(url_for("livros"))


@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():
    if request.method == "POST":
        nome = request.form.get("nome_completo", "").strip()
        data_nascimento = request.form.get("data_nascimento", "").strip()
        cpf = limpar_cpf(request.form.get("cpf"))

        if not nome or not data_nascimento or not cpf:
            flash("Preencha nome, data de nascimento e CPF.", "erro")
            return redirect(url_for("usuarios"))

        if not validar_cpf(cpf):
            flash("CPF invalido.", "erro")
            return redirect(url_for("usuarios"))

        if buscar_cpf_usuario(cpf):
            flash("Este CPF ja esta cadastrado.", "erro")
            return redirect(url_for("usuarios"))

        salvar_usuario(nome.upper(), data_nascimento, cpf)
        flash("Usuario cadastrado com sucesso.", "sucesso")
        return redirect(url_for("usuarios"))

    busca = request.args.get("busca", "").strip()
    parametros = []
    sql = "SELECT * FROM usuarios WHERE 1 = 1"

    if busca:
        sql += " AND (nome_completo LIKE ? OR cpf LIKE ?)"
        termo = f"%{busca}%"
        parametros.extend([termo, termo])

    sql += " ORDER BY nome_completo ASC"
    lista_usuarios = consultar(sql, parametros)

    return render_template("usuarios.html", usuarios=lista_usuarios, busca=busca)


@app.route("/usuarios/<cpf>/editar", methods=["GET", "POST"])
def editar_usuario(cpf):
    cpf = limpar_cpf(cpf)
    usuario = consultar("SELECT * FROM usuarios WHERE cpf = ?", (cpf,), unico=True)
    if not usuario:
        flash("Usuario nao encontrado.", "erro")
        return redirect(url_for("usuarios"))

    if request.method == "POST":
        nome = request.form.get("nome_completo", "").strip()
        data_nascimento = request.form.get("data_nascimento", "").strip()
        novo_cpf = limpar_cpf(request.form.get("cpf"))

        if not nome or not data_nascimento or not novo_cpf:
            flash("Preencha nome, data de nascimento e CPF.", "erro")
            return redirect(url_for("editar_usuario", cpf=cpf))

        if not validar_cpf(novo_cpf):
            flash("CPF invalido.", "erro")
            return redirect(url_for("editar_usuario", cpf=cpf))

        cpf_ja_usado = buscar_cpf_usuario(novo_cpf)
        if novo_cpf != cpf and cpf_ja_usado:
            flash("Este CPF ja esta cadastrado.", "erro")
            return redirect(url_for("editar_usuario", cpf=cpf))

        executar(
            """
            UPDATE usuarios
            SET nome_completo = ?, data_nascimento = ?, cpf = ?
            WHERE cpf = ?
            """,
            (nome.upper(), data_nascimento, novo_cpf, cpf),
        )
        executar("UPDATE emprestimos SET cpf = ?, nome_usuario = ?, data_nascimento_usuario = ? WHERE cpf = ?", (novo_cpf, nome.upper(), data_nascimento, cpf))
        flash("Usuario atualizado com sucesso.", "sucesso")
        return redirect(url_for("usuarios"))

    return render_template("editar_usuario.html", usuario=usuario)


@app.route("/usuarios/<cpf>/excluir", methods=["POST"])
def excluir_usuario_web(cpf):
    cpf = limpar_cpf(cpf)
    usuario = buscar_usuario_por_cpf(cpf)
    if not usuario:
        flash("Usuario nao encontrado.", "erro")
    elif usuario[4] > 0:
        flash("Nao e possivel excluir usuario com livros emprestados.", "erro")
    else:
        excluir_usuario_banco_dados(cpf)
        flash("Usuario excluido com sucesso.", "sucesso")
    return redirect(url_for("usuarios"))


@app.route("/emprestimos", methods=["GET", "POST"])
def emprestimos():
    if request.method == "POST":
        cpf = limpar_cpf(request.form.get("cpf"))
        id_livro = request.form.get("id_livro", "").strip()
        data_vencimento = request.form.get("data_vencimento", "").strip()

        if not cpf or not id_livro or not data_vencimento:
            flash("Escolha usuario, livro e data de vencimento.", "erro")
            return redirect(url_for("emprestimos"))

        try:
            id_livro = int(id_livro)
        except ValueError:
            flash("Livro invalido.", "erro")
            return redirect(url_for("emprestimos"))

        usuario = buscar_usuario_por_cpf(cpf)
        livro = buscar_livro_id(id_livro)

        if not usuario:
            flash("Usuario nao encontrado.", "erro")
            return redirect(url_for("emprestimos"))

        if not livro:
            flash("Livro nao encontrado.", "erro")
            return redirect(url_for("emprestimos"))

        if livro[5] == 0:
            flash("Este livro ja esta emprestado.", "erro")
            return redirect(url_for("emprestimos"))
        
        if usuario[4] > 2:
            flash("Limite maximo de livros emprestado para este usuario.", "erro")
            return redirect(url_for("emprestimos"))

        salvar_emprestimo(
            cpf,
            usuario[1],
            usuario[2],
            livro[0],
            livro[1],
            date.today().isoformat(),
            data_vencimento,
        )
        editar_status_livro(livro[0], 0)
        editar_livros_emprestado_usuario(cpf, usuario[4] + 1)
        flash("Emprestimo registrado com sucesso.", "sucesso")
        return redirect(url_for("emprestimos"))

    lista_emprestimos = consultar("SELECT rowid, * FROM emprestimos ORDER BY data_vencimento ASC")
    usuarios_cadastrados = consultar("SELECT * FROM usuarios ORDER BY nome_completo ASC")
    livros_disponiveis = consultar("SELECT * FROM livros WHERE status = 1 ORDER BY nome_livro ASC")

    return render_template(
        "emprestimos.html",
        emprestimos=lista_emprestimos,
        usuarios=usuarios_cadastrados,
        livros=livros_disponiveis,
    )


@app.route("/emprestimos/<int:id_emprestimo>/devolver", methods=["POST"])
def devolver_emprestimo(id_emprestimo):
    emprestimo = consultar("SELECT rowid, * FROM emprestimos WHERE rowid = ?", (id_emprestimo,), unico=True)
    if not emprestimo:
        flash("Emprestimo nao encontrado.", "erro")
        return redirect(url_for("emprestimos"))

    usuario = buscar_usuario_por_cpf(emprestimo["cpf"])
    editar_status_livro(emprestimo["id_livro"], 1)

    if usuario:
        editar_livros_emprestado_usuario(emprestimo["cpf"], max(usuario[4] - 1, 0))

    executar("DELETE FROM emprestimos WHERE rowid = ?", (id_emprestimo,))
    flash("Devolucao registrada com sucesso.", "sucesso")
    return redirect(url_for("emprestimos"))


preparar_banco()


if __name__ == "__main__":
    app.run(debug=True)
