from Cadastros.cadastrar_usuario import coletar_cpf_usuario
from Banco.db_config import editar_cpf_usuario, buscar_cpf_usuario
from Utils.limparchat import limpar_chat

def editando_cpf_usuario(cpf_usuario):
    print("\n======= EDITANDO CPF DO USUARIO =======")
    novo_cpf_usuario = coletar_cpf_usuario()
    if novo_cpf_usuario is None:
        limpar_chat()
        return False
    if buscar_cpf_usuario(novo_cpf_usuario):
        limpar_chat()
        print("Erro: Esse CPF já está cadastrado no banco de dados!")
        return False
    editar_cpf_usuario(cpf_usuario, novo_cpf_usuario)
    limpar_chat()
    print("Sistema: CPF do usuario alterado com sucesso!")
    return novo_cpf_usuario
