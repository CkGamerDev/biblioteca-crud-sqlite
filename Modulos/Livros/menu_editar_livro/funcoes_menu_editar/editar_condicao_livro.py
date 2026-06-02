from Importantes.db_config import editar_condicao_livro, buscar_livro_id
from Importantes.limparchat import limpar_chat

def funcao_editar_condicao(index):   
    limpar_chat() 
    print("========== EDITANDO CONDIÇÃO DO LIVRO ==========")
    novo_condicao = escolher_novo_condicao()
    editar_condicao_livro(index, novo_condicao)
    livro = buscar_livro_id(index)
    mostrar_livro(livro)


def escolher_novo_condicao():
    while True:
        novo_condicao = input("Digite a nova condição do livro: ").upper().strip()
        if novo_condicao == "":
            print("\nErro: A nova condição não pode estar vazia! ")
        else:
            return novo_condicao
        

def mostrar_livro(livro):
    limpar_chat()
    print("\n======= CONDIÇÃO DO LIVRO ALTERADO =======")
    print(f"""
ID: {livro[0]}
Nome: {livro[1].title()}
Descrição: {livro[2]}
Condição: {livro[3].capitalize()}
Entregue por: {livro[4].title()}
""")
    print("================================\n\n")