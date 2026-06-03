from Utils.limparchat import limpar_chat
from Pesquisas.Livros.procurar_nome import pesquisar_livro_nome
from Pesquisas.Livros.procurar_id import pesquisar_livro_id
from Pesquisas.Livros.procurar_todos import pesquisar_todos_livros
from Pesquisas.Livros.procurar_disponiveis import pesquisar_livros_disponiveis
from Pesquisas.Livros.procurar_emprestados import pesquisar_livros_emprestados

def mostrar_menu():
    print("===== MENU DE PROCURA =====")
    print("1 - Pesquisar por nome")
    print("2 - Pesquisar por id")
    print("3 - Mostrar todos")
    print("4 - Livros disponiveis")
    print("5 - Livros emprestados")
    print("6 - Sair")

def selecionar_op():
    while True:
        try:
            op = int(input("\nDigite a opção desejada: "))
            return op
        except ValueError:
            print("\nErro: Use apenas numeros!")


def menu_procura():
    while True:
        mostrar_menu()
        op = selecionar_op()
        if op == 1:
            limpar_chat()
            pesquisar_livro_nome()
        if op == 2:
            limpar_chat()
            pesquisar_livro_id()
        if op == 3:
            limpar_chat()
            pesquisar_todos_livros()
        if op == 4:
            limpar_chat()
            pesquisar_livros_disponiveis()#testar função depois que criar sistema de emprestar livro!
        if op == 5:
            limpar_chat()
            pesquisar_livros_emprestados()
        elif op == 6:
            limpar_chat()
            break
        elif op < 1 or op > 6:
            print("\nErro: Opção invalida!")