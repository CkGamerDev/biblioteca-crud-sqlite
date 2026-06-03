from Utils.limparchat import limpar_chat
from Menus.menu_principal_livros import menu_livros

def mostrar_menu():
    print("===== BIBIOTLECA MENU =====")
    print("1 - Menu de livros")
    print("2 - Menu de Usuarios")
    print("3 - Sair")

def selecionar_op():
    while True:
        try:
            op = int(input("\nDigite a opção desejada: "))
            return op
        except ValueError:
            print("\nErro: Use apenas numeros!")


def menu_inicial():
    while True:
        mostrar_menu()
        op = selecionar_op()
        if op == 1:
            limpar_chat()
            menu_livros()
        elif op == 2:
            limpar_chat()
            print("\nSistema: Fechando bibiotleca....")
            break
        elif op < 1 or op > 3:
            print("\nErro: Opção invalida!")