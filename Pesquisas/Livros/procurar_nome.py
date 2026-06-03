from Banco.db_config import buscar_livro_nome
from Utils.limparchat import limpar_chat

def nome_livro():
    while True:
        print("=============== PROCURANDO LIVRO POR NOME ===============")
        nome = input("\nDigite o nome do livro: ").upper().strip()
        if not nome:
            return None
        else:
            return nome

def mostrar_livros_encontrados(livros):
    limpar_chat()
    print("======= LIVROS ENCONTRADOS =======")
    for livro in livros:
        print(f"""
---------------------------------------
ID: {livro[0]}
Nome: {livro[1].title()}
Descrição: {livro[2]}
Condição: {livro[3].capitalize()}
Entregue por: {livro[4].title()}
---------------------------------------
""")
    print("==================================\n\n")


def pesquisar_livro_nome():
    nome = nome_livro()
    if nome is None:
        limpar_chat()
        print("\nSistema: Busca cancelada!\n")
    else:
        livros = buscar_livro_nome(nome)
        if not livros:
            limpar_chat()
            print("\nSistema: Nenhum livro encontrado!\n")
            return
        mostrar_livros_encontrados(livros)

    