from Cadastros.cadastrar_usuario import coletar_nome_usuario
from Banco.db_config import editar_nome_usuario
from Utils.limparchat import limpar_chat

def editando_nome_usuario(cpf_usuario):
    print("\n======= EDITANDO NOME DE USUARIO =======")
    novo_nome = coletar_nome_usuario()
    if novo_nome is None:
        limpar_chat()
        return False
    editar_nome_usuario(cpf_usuario, novo_nome)
    limpar_chat()
    print("Sistema: Nome de usuario alterado com sucesso! ")
    return True
