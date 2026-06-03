from Banco.db_config import editar_nome_livro, buscar_livro_id
from Utils.limparchat import limpar_chat

def funcao_editar_nome(index):  
    limpar_chat() 
    print("========== EDITANDO NOME DO LIVRO ==========")
    novo_nome = escolher_novo_nome()
    editar_nome_livro(index, novo_nome)
    livro = buscar_livro_id(index)
    mostrar_livro(livro)


def escolher_novo_nome():
    while True:
        novo_nome = input("Digite o novo nome do livro: ").upper().strip()
        if novo_nome == "":
            print("\nErro: O novo nome não pode estar vazio! ")
        else:
            return novo_nome
        

def mostrar_livro(livro):
    limpar_chat()
    print("\n======= NOME DO LIVRO ALTERADO =======")
    print(f"""
ID: {livro[0]}
Nome: {livro[1].title()}
Descrição: {livro[2]}
Condição: {livro[3].capitalize()}
Entregue por: {livro[4].title()}
""")
    print("================================\n\n")