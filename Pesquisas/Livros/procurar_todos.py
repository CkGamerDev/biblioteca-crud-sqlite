from Utils.limparchat import limpar_chat
from Banco.db_config import buscar_todos_livros

def mostrar_livros(livros):
    limpar_chat()
    print("\n======= TODOS OS LIVROS =======")
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



def pesquisar_todos_livros():
    livros = buscar_todos_livros()

    if not livros:
        print("Sistema: Nenhum livro cadastrado! ")
        return
    
    mostrar_livros(livros)
    
