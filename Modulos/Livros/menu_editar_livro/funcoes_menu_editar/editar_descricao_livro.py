from Importantes.db_config import editar_descricao_livro, buscar_livro_id
from Importantes.limparchat import limpar_chat

def funcao_editar_descricao(index):
    limpar_chat() 
    print("========== EDITANDO DESCRIÇÃO DO LIVRO ==========")   
    nova_descricao = escolher_nova_descricao()
    editar_descricao_livro(index, nova_descricao)
    livro = buscar_livro_id(index)
    mostrar_livro(livro)


def escolher_nova_descricao():
    nova_descricao = input("Digite a nova descrição do livro: ").strip()
    if not nova_descricao:
        nova_descricao = "Sem descrição"
    return nova_descricao
        

def mostrar_livro(livro):
    limpar_chat()
    print("\n======= DESCRIÇÃO DO LIVRO ALTERADO =======")
    print(f"""
ID: {livro[0]}
Nome: {livro[1].title()}
Descrição: {livro[2]}
Condição: {livro[3].capitalize()}
Entregue por: {livro[4].title()}
""")
    print("================================\n\n")