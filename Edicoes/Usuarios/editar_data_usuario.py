from Cadastros.cadastrar_usuario import coletar_data_nascimento_usuario
from Banco.db_config import editar_data_nascimento_usuario
from Utils.limparchat import limpar_chat

def editando_data_usuario(cpf_usuario):
    print("\n======= EDITANDO DATA DE NASCIMENTO DO USUARIO =======")
    nova_data = coletar_data_nascimento_usuario()
    if nova_data is None:
        limpar_chat()
        return False
    editar_data_nascimento_usuario(cpf_usuario, nova_data)
    limpar_chat()
    print("Sistema: Data de nascimento alterada com sucesso!")
    return True
