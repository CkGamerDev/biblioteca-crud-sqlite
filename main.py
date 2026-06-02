from menu import menu_inicial
from Importantes.db_config import criar_tabelas
from Importantes.limparchat import limpar_chat

if __name__ == "__main__":
    criar_tabelas()
    limpar_chat()
    menu_inicial()