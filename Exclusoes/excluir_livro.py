from Utils.limparchat import limpar_chat
from Pesquisas.Livros.procurar_id import pesquisar_livro_id
from Banco.db_config import excluir_livro, buscar_livro_id

def mostrar_menu():
    print("\n========== EXCLUIR LIVRO ? ==========")
    print("1 - SIM")
    print("2 - NÃO")

def selecionar_op():
    while True:
        try:
            op = int(input("\nDigite a opção desejada: "))
            return op
        except ValueError:
            print("\nErro: Use apenas numeros!")


def mostrar_livro(livro):
    limpar_chat()
    print("\n======= LIVRO EXCLUIDO =======")
    print(f"""
ID: {livro[0]}
Nome: {livro[1].title()}
Descrição: {livro[2]}
Condição: {livro[3].capitalize()}
Entregue por: {livro[4].title()}
""")
    print("================================\n\n")


def funcao_excluir_livro():
    index = pesquisar_livro_id()
    if index is None:
        return
    mostrar_menu()
    while True:
        op = selecionar_op()
        if op == 1:
            livro = buscar_livro_id(index)
            mostrar_livro(livro)
            excluir_livro(index)
            break
        elif op == 2:
            limpar_chat()
            print("Sistema: Exclusão cancelada! ")
            break
        elif op < 1 or op > 2:
            print("\nErro: Opção invalida!")



    
