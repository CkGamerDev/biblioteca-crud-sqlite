from Validacoes.validar_cpf import validar_cpf
from Banco.db_config import buscar_cpf_usuario, buscar_usuario_por_cpf
from Utils.limparchat import limpar_chat

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

def mostrar_informacoes_usuario(cpf_usuario):
    usuario = buscar_usuario_por_cpf(cpf_usuario)
    print("\n======= INFORMAÇÕES DO USUÁRIO =======")
    print(f"ID: {usuario[0]}")
    print(f"Nome: {usuario[1]}")
    print(f"Data de nascimento: {usuario[2]}")
    print(f"CPF: {usuario[3]}")
    print(f"Livros emprestados: {usuario[4]}")
    print("========================================")


def pesquisar_usuario():
    print("======= CONSULTA DE USUARIO =======")
    cpf_usuario = coletar_cpf_usuario()
    if cpf_usuario is None:
        limpar_chat()
        return False
    limpar_chat()
    if not buscar_cpf_usuario(cpf_usuario):
        limpar_chat()
        print("Erro: Esse CPF não existe no banco de dados!\n")
        return False
    mostrar_informacoes_usuario(cpf_usuario)
    return cpf_usuario