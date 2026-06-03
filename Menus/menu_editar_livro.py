from Utils.limparchat import limpar_chat
from Edicoes.Livros.editar_livro import funcao_menu_editando 
from Exclusoes.excluir_livro import funcao_excluir_livro

def mostrar_menu():
    print("===== MENU DE EDITAR LIVRO =====")
    print("1 - Editar livro")
    print("2 - Excluir livro")
    print("3 - Sair")

def selecionar_op():
    while True:
        try:
            op = int(input("\nDigite a opção desejada: "))
            return op
        except ValueError:
            print("\nErro: Use apenas numeros!")


def funcao_menu_inicial():
    while True:
        mostrar_menu()
        op = selecionar_op()
        if op == 1:
            limpar_chat()
            funcao_menu_editando()
        if op == 2:
            limpar_chat()
            funcao_excluir_livro()
        elif op == 3:
            limpar_chat()
            break
        elif op < 1 or op > 3:
            print("\nErro: Opção invalida!")