from Menus.menu_principal_sistema import menu_inicial
from Banco.db_config import criar_tabelas
from Utils.limparchat import limpar_chat

if __name__ == "__main__":
    criar_tabelas()
    limpar_chat()
    menu_inicial()