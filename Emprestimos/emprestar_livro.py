from Pesquisas.Usuarios.pesquisar_usuario import pesquisar_usuario
from Utils.limparchat import limpar_chat
from Banco.db_config import salvar_emprestimo, buscar_usuario_por_cpf, buscar_cpf_usuario, editar_status_livro, editar_livros_emprestado_usuario, buscar_livro_id
from Validacoes.validar_cpf import validar_cpf

def pegar_id_livro():
    limpar_chat()
    while True:
        print("=============== QUAL LIVRO ESTÁ EMPRESTANDO? ===============")
        try:
            index = int(input("Digite o id do livro: "))
            livro = buscar_livro_id(index)
            if not livro:
                return False
            return index, livro
        except ValueError:
            print("Erro: Use apenas numeros!")


#====================================USUARIOS========================================#
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

def procurar_usuario():
    print("======= QUEM ESTÁ EMPRESTANDO? =======")
    cpf_usuario = coletar_cpf_usuario()
    if cpf_usuario is None:
        limpar_chat()
        return False
    limpar_chat()
    if not buscar_cpf_usuario(cpf_usuario):
        limpar_chat()
        print("Erro: Esse CPF não existe no banco de dados!\n")
        return False
    usuario = buscar_usuario_por_cpf(cpf_usuario)
    return cpf_usuario, usuario

def confirmar_usuario():
    while True:
        print("1 - SIM\n2 - NÃO")
        try:
            confirmar = int(input("Confirmar usuario? "))
            if confirmar == 1:
                return True
            if confirmar == 2:
                return False
            print("Erro: Opção invalida!")
        except ValueError:
            print("Erro: Use apenas numeros! ")
#==================================FIM USUARIOS==========================================#

def funcao_emprestar_livro():
    while True:
        cpf_usuario, usuario = procurar_usuario()
        if cpf_usuario is None:
            return False
        
        if confirmar_usuario() == False:
            return False
        
        index, livro = pegar_id_livro()
        if index is False:
            print("Sistema: Livro não encontrado!")
            return False
        
        if livro[5] == 0:
            print("Sistema: Este livro está indisponivel!")

    #vereficar qual livro ele quer emprestar(vereficar se existe estoque disponivel para emprestar)
    #verefica se o usuario está com o limete de livros emprestado
    #salvar no banco o livro emprestado
    #alterar o estoque do livro no banco
