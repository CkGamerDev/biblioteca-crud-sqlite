from Utils.limparchat import limpar_chat
from Cadastros.cadastrar_usuario import cadastro_usuario
from Pesquisas.Usuarios.pesquisar_usuario import pesquisar_usuario

def mostrar_menu():
    print("===== MENU DE USUARIOS =====")
    print("1 - Cadastrar")
    print("2 - Vereficar status")
    print("3 - Editar")
    print("4 - Excluir")
    print("5 - Sair")

def selecionar_op():
    while True:
        try:
            op = int(input("\nDigite a opção desejada: "))
            return op
        except ValueError:
            print("\nErro: Use apenas numeros!")


def menu_principal_usuarios():
    while True:
        mostrar_menu()
        op = selecionar_op()
        if op == 1:
            limpar_chat()
            cadastro_usuario()
        if op == 2:
            limpar_chat()
            pesquisar_usuario()
        elif op == 5:
            limpar_chat()
            break
        elif op < 1 or op > 3:
            print("\nErro: Opção invalida!")