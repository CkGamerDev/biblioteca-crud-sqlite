from Importantes.db_config import editar_entregue_livro, buscar_livro_id
from Importantes.limparchat import limpar_chat

def funcao_editar_entregue(index):  
    limpar_chat() 
    print("========== EDITANDO ENTREGUE DO LIVRO ==========") 
    novo_entregue = escolher_novo_entregue()
    editar_entregue_livro(index, novo_entregue)
    livro = buscar_livro_id(index)
    mostrar_livro(livro)


def escolher_novo_entregue():
    while True:
        novo_entregue = input("Digite o novo entregue do livro: ").upper().strip()
        if novo_entregue == "":
            print("\nErro: O novo entregue não pode estar vazio!  ")
        else:
            return novo_entregue
        

def mostrar_livro(livro):
    limpar_chat()
    print("\n======= ENTREGUE DO LIVRO ALTERADO =======")
    print(f"""
ID: {livro[0]}
Nome: {livro[1].title()}
Descrição: {livro[2]}
Condição: {livro[3].capitalize()}
Entregue por: {livro[4].title()}
""")
    print("================================\n\n")