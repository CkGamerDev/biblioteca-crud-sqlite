from Importantes.limparchat import limpar_chat
from Importantes.db_config import buscar_livros_emprestados

def mostrar_livros(livros):
    limpar_chat()
    print("\n======= LIVROS EMPRESTADOS =======")
    for livro in livros:
        id_livro = livro[0]
        nome_livro = livro[1]
        descricao = livro[2]
        estado_livro = livro[3]
        entregue_por = livro[4]
        print(f"""
-------------------------------------
ID: {id_livro}
Nome: {nome_livro.title()}
Descrição: {descricao.capitalize()}
Condição: {estado_livro.capitalize()}
Entregue por: {entregue_por.title()}
-------------------------------------
""")



def pesquisar_livros_emprestados():
    livros = buscar_livros_emprestados()
    if not livros:
        print("\nSistema: Nenhum livro emprestado! ")
        return
    mostrar_livros(livros)