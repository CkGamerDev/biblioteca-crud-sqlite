from Utils.limparchat import limpar_chat
from Cadastros.cadastrar_usuario import coletar_cpf_usuario
from Banco.db_config import buscar_cpf_usuario, excluir_usuario_banco_dados
from Pesquisas.Usuarios.pesquisar_usuario import mostrar_informacoes_usuario

def mostrar_menu():
    print("\n========== EXCLUIR USUARIO ==========")
    print("1 - SIM")
    print("2 - NÃO")

def selecionar_op():
    while True:
        try:
            op = int(input("Escolha: "))
            return op
        except ValueError:
            print("\nErro: Use apenas numeros!")


def excluir_usuario():
    print("======= PROCURANDO CPF PARA EXCLUSÃO =======")
    cpf_usuario = coletar_cpf_usuario()
    if cpf_usuario is None:
        limpar_chat()
        return
    if not buscar_cpf_usuario(cpf_usuario):
        limpar_chat()
        print("Erro: Esse CPF não está cadastrado no banco de dados!\n")
        return False
    while True:
        limpar_chat()
        mostrar_informacoes_usuario(cpf_usuario)
        mostrar_menu()
        op = selecionar_op()
        if op == 1:
            limpar_chat()
            print("======= USUARIO DELETADO COM SUCESSO =======")
            excluir_usuario_banco_dados(cpf_usuario)
            break
        elif op == 2:
            limpar_chat()
            print("Sistema: Exclusão cancelada! ")
            break
        elif op < 1 or op > 2:
            print("\nErro: Opção invalida!")



    
