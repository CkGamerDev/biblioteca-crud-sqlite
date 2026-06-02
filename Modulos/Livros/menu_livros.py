from Importantes.limparchat import limpar_chat
from Modulos.Livros.cadastrar_livro import cadastro_livros
from Modulos.Livros.menu_procura.menu_procurar import menu_procura
from Modulos.Livros.menu_editar_livro.menu_editar import funcao_menu_inicial

def mostrar_menu():
    print("===== MENU DE LIVROS =====")
    print("1 - Cadastrar novo livro")
    print("2 - Menu de procura")
    print("3 - Editar um livro")
    print("4 - Voltar ao menu")

def selecionar_op():
    while True:
        try:
            op = int(input("\nDigite a opção desejada: "))
            return op
        except ValueError:
            print("\nErro: Use apenas numeros!")


def menu_livros():
    while True:
        mostrar_menu()
        op = selecionar_op()
        if op == 1:
            limpar_chat()
            cadastro_livros()
        elif op == 2:
            limpar_chat()
            menu_procura()
        elif op == 3:
            limpar_chat()
            funcao_menu_inicial()
        elif op == 4:
            limpar_chat()
            break
        elif op < 1 or op > 4:
            print("\nErro: Opção invalida!")