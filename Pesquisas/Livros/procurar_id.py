from Utils.limparchat import limpar_chat
from Banco.db_config import buscar_livro_id

def pegar_id():
    while True:
        print("=============== PROCURANDO LIVRO POR ID ===============")
        try:
            index = int(input("Digite o id do livro: "))
            return index
        except ValueError:
            print("Erro: Use apenas numeros!")

def mostrar_livro(livro):
    limpar_chat()
    print("\n======= LIVRO ENCONTRADO =======")
    print(f"""
ID: {livro[0]}
Nome: {livro[1].title()}
Descrição: {livro[2]}
Condição: {livro[3].capitalize()}
Entregue por: {livro[4].title()}
""")
    print("================================\n\n")

def pesquisar_livro_id():
    index = pegar_id()
    limpar_chat()
    livro = buscar_livro_id(index)
    if not livro:
        print("Sistema: Livro não encontrado!\n")
        return
    mostrar_livro(livro)
    return index
    

