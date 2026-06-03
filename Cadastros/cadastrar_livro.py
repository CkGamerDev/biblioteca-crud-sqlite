from Utils.limparchat import limpar_chat
from Banco.db_config import salvar_livro

def nome_livro():
    while True:
        nome_livro = input("\nNome do Livro: ")
        if nome_livro == "":
            print("\nErro: O nome do livro não pode ser vazio!")
        else:
            return nome_livro.strip().upper()

def descricao_livro():
    descricao = input("\nDescrição do livro: ")
    if descricao == "":
        descricao = "Sem descrição"
    return descricao

def condicoes_livro():
    while True:
        cond = input("\nQual a condição do livro: ")
        if cond == "":
            cond = "Não definido"
        else:
            return cond.strip().upper()


def entregue_por():
    while True:
        nome = input("\nQuem entregou este livro: ")
        if nome == "":
            print("\nErro: O nome não pode estar vazio!")
        else:
            return nome.strip().upper()
    
def mostrar_livro_cadastrado(nome, descricao, estado_livro, entregue):
    limpar_chat()
    print("======= LIVRO CADASTRADO =======")
    print(f"Nome do livro: {nome.title()}")
    print(f"Descrição: {descricao}")
    print(f"Condição do livro: {estado_livro.upper()}")
    print(f"Entregue por: {entregue.title()}")
    print("=====================================\n\n")

def confirmar_cadastro():
    while True:
        print("\n=============== CONFIRMAR O CADASTR0 DESTE LIVRO? ===============")
        try:
            confirmar = int(input("1 - SIM\n2 - NÃO\nESCOLHA:"))
            if confirmar < 1 or confirmar > 2:
                print("Erro: Opção invalida!")
            else:
                return confirmar
        except ValueError:
            print("Erro: Use apenas numeros! ")
    

def cadastro_livros():
    print("=============== CADASTRANDO NOVO LIVRO ===============")
    nome = nome_livro()
    limpar_chat()
    print("=============== CADASTRANDO NOVO LIVRO ===============")
    print(f"Nome do livro: {nome.title()}")
    descricao = descricao_livro()
    limpar_chat()
    print("=============== CADASTRANDO NOVO LIVRO ===============")
    print(f"Nome do livro: {nome.title()} \nDescrição: {descricao}")
    estado_livro = condicoes_livro()
    limpar_chat()
    print("=============== CADASTRANDO NOVO LIVRO ===============")
    print(f"Nome do livro: {nome.title()} \nDescrição: {descricao} \nCondição do livro: {estado_livro}")
    entregue = entregue_por()
    limpar_chat()
    print("=============== CADASTRANDO NOVO LIVRO ===============")
    print(f"Nome do livro: {nome.title()} \nDescrição: {descricao} \nCondição do livro: {estado_livro} \nEntregue por: {entregue.title()}")
    confirmar = confirmar_cadastro()
    if confirmar == 1:
        mostrar_livro_cadastrado(nome, descricao, estado_livro, entregue)
        salvar_livro(nome, descricao, estado_livro, entregue)
    elif confirmar == 2:
        limpar_chat()
        print("\nSistema: Livro não cadastrado!")