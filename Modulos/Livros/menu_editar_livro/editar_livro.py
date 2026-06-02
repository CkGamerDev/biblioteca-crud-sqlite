from Importantes.limparchat import limpar_chat
from Modulos.Livros.menu_procura.procurar_id import pesquisar_livro_id
from Modulos.Livros.menu_editar_livro.funcoes_menu_editar.editar_nome_livro import funcao_editar_nome
from Modulos.Livros.menu_editar_livro.funcoes_menu_editar.editar_descricao_livro import funcao_editar_descricao 
from Modulos.Livros.menu_editar_livro.funcoes_menu_editar.editar_condicao_livro import funcao_editar_condicao 
from Modulos.Livros.menu_editar_livro.funcoes_menu_editar.editar_entregue_livro import funcao_editar_entregue

def mostrar_menu():
    print("\n========== EDITANDO LIVRO ==========")
    print("1 - Editar nome")
    print("2 - Editar descrição")
    print("3 - Editar condição")
    print("4 - Editar entregue")
    print("5 - Sair")

def selecionar_op():
    while True:
        try:
            op = int(input("\nDigite a opção desejada: "))
            return op
        except ValueError:
            print("\nErro: Use apenas numeros!")


def funcao_menu_editando():
    index = pesquisar_livro_id()
    if index is None:
        return
    while True:
        mostrar_menu()
        op = selecionar_op()
        if op == 1:
            funcao_editar_nome(index)
        if op == 2:
            funcao_editar_descricao(index)
        if op == 3:
            funcao_editar_condicao(index)
        if op == 4:
            funcao_editar_entregue(index)
        elif op == 5:
            limpar_chat()
            break
        elif op < 1 or op > 5:
            print("\nErro: Opção invalida!")


    
