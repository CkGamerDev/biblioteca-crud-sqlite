from Validacoes.validar_cpf import validar_cpf
from Banco.db_config import buscar_cpf_usuario, salvar_usuario
from datetime import datetime
from Utils.limparchat import limpar_chat

def coletar_cpf_usuario():
    while True:
        cpf = input("Digite o CPF do usuario: ").strip()
        if not cpf:
            print("\nErro: O CPF não pode ser vazio! ")
        else:
           if validar_cpf(cpf):
               return cpf


def coletar_nome_usuario():
    while True:
        nome_usuario = input("Digite o nome do usuario: ").strip()
        if not nome_usuario:
            print("\nErro: Usuario sem nome.")
        else:
            if any(caractere.isdigit() for caractere in nome_usuario):
                print("\nErro: O nome de usuario não pode conter numeros.")
            else:
                return nome_usuario
            
def coletar_data_nascimento_usuario():
    while True:
        data = input("Digite a data de nascimento (DD/MM/AAAA): ").strip()
        try:
            data_convertida = datetime.strptime(data, "%d/%m/%Y").date()
            hoje = datetime.today().date()
            if data_convertida > hoje:
                print("\nErro: Data inválida! ")
                continue
            return data_convertida
        except ValueError:
            print("\nErro: Data invalida.")

def confirmar_cadastro_usuario():
    while True:
        print("\n====== CONFIRMAR CADASTRO DE USUARIO ======")
        print("1 - SIM")
        print("2 - NÃO")
        try:
            op = int(input("ESCOLHA: "))
            if op < 1 or op > 2:
                print("\nErro: Opção invalida! \n")
            elif op == 1:
                return True
            elif op == 2:
                return False
        except ValueError:
            print("\nErro: Digite apenas numeros (1 ou 2).")

def mostrar_cadastro_concluido(nome, data, cpf):
    limpar_chat()
    print("====== USUARIO CADASTRADO COM SUCESSO =======")
    print(f"Nome: {nome.title()}")
    print(f"CPF: {cpf}")
    print(f"Data de Nascimento: {data}")
    print("=============================================\n")


def cadastro_usuario():
    limpar_chat()
    print("======= CADASTRANDO USUARIO =======")
    cpf_usuario = coletar_cpf_usuario()
    limpar_chat()
    print("======= CADASTRANDO USUARIO =======")
    print(f"CPF: {cpf_usuario}\n")

    if buscar_cpf_usuario(cpf_usuario):
        limpar_chat()
        print("Erro: Esse CPF já está cadastrado no banco de dados!\n")
        return False
    
    nome_usuario = coletar_nome_usuario()
    limpar_chat()
    print("======= CADASTRANDO USUARIO =======")
    print(f"CPF: {cpf_usuario}\nNome: {nome_usuario}\n")

    data_nascimento = coletar_data_nascimento_usuario()
    limpar_chat()
    print("======= CADASTRANDO USUARIO =======")
    print(f"CPF: {cpf_usuario}\nNome: {nome_usuario}\nData de Nascimento: {data_nascimento}\n")

    if confirmar_cadastro_usuario():
        salvar_usuario(nome_usuario.upper(), data_nascimento, cpf_usuario)
        mostrar_cadastro_concluido(nome_usuario, data_nascimento, cpf_usuario)
    else:
        print("Sistema: Cadastro de usuario cancelado! \n")