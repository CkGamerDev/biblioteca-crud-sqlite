from Utils.limparchat import limpar_chat
from Emprestimos.emprestar_livro import funcao_emprestar_livro

def mostrar_menu():
    print("===== MENU DE EMPRESTIMO =====")
    print("1 - Emprestar livro")
    print("2 - Devolver livro")
    print("3 - Livros atrasados")
    print("4 - Voltar ao menu")

def selecionar_op():
    while True:
        try:
            op = int(input("\nDigite a opção desejada: "))
            return op
        except ValueError:
            print("\nErro: Use apenas numeros!")


def menu_emprestimos():
    while True:
        mostrar_menu()
        op = selecionar_op()
        if op == 1:
            limpar_chat()
            funcao_emprestar_livro()
        elif op == 2:
            limpar_chat()
        elif op == 3:
            limpar_chat()
        elif op == 4:
            limpar_chat()
            break
        elif op < 1 or op > 4:
            print("\nErro: Opção invalida!")