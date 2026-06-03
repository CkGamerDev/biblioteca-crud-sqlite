from Menus.menu_principal_sistema import menu_inicial
from Banco.criar_tabela_livro import cria_tabela_livros
from Banco.criar_tabela_usuarios import cria_tabela_usuarios
from Utils.limparchat import limpar_chat

if __name__ == "__main__":
    cria_tabela_livros()
    cria_tabela_usuarios()
    limpar_chat()
    menu_inicial()