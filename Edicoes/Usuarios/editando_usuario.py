from Utils.limparchat import limpar_chat
from Validacoes.validar_cpf import validar_cpf
from Banco.db_config import buscar_cpf_usuario
from Pesquisas.Usuarios.pesquisar_usuario import mostrar_informacoes_usuario
from Edicoes.Usuarios.editar_nome_usuario import editando_nome_usuario
from Edicoes.Usuarios.editar_data_usuario import editando_data_usuario
from Edicoes.Usuarios.editando_cpf_usuario import editando_cpf_usuario

def coletar_cpf_usuario():
    while True:
        print("0 - Sair")
        cpf = input("Digite o CPF do usuario: ").strip()
        if not cpf:
            print("\nErro: O CPF não pode ser vazio! ")
        else:
           if cpf == "0":
                return None
           if validar_cpf(cpf):
               return cpf

def escolher_opcao_editar():
    while True:
        try:
            op = int(input("Digite a opção desejada para editar: "))
            return op
        except ValueError:
            print("\nErro: Use apenas numeros. ")


def mostrar_opcao_editar():
    print("====== EDITAR ======")
    print("1 - Nome de usuario")
    print("2 - Data de nascimento")
    print("3 - CPF do usuario")
    print("4 - Sair")


def editar_usuario():
    print("======= PROCURANDO USUARIO PARA EDITAR =======")
    cpf_usuario = coletar_cpf_usuario()
    if cpf_usuario is None:
        limpar_chat()
        return False
    if not buscar_cpf_usuario(cpf_usuario):
        limpar_chat()
        print("Erro: Esse CPF não existe no banco de dados!\n")
        return False
    limpar_chat()
    while True: 
        mostrar_informacoes_usuario(cpf_usuario)
        mostrar_opcao_editar()
        op = escolher_opcao_editar()
        if op == 1:
            editando_nome_usuario(cpf_usuario)
        if op == 2:
            editando_data_usuario(cpf_usuario)
        if op == 3:
            novo_cpf_usuario = editando_cpf_usuario(cpf_usuario)
            cpf_usuario = novo_cpf_usuario
        if op == 4:
            limpar_chat()
            return False
        if op < 1 or op > 4:
            print("Erro: Opção invalida! ")

    