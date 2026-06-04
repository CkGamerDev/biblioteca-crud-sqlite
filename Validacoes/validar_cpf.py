def validar_cpf(cpf):
    # Remove pontos e traços
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os números são iguais
    if cpf == cpf[0] * 11:
        return False

    # ==========================
    # Primeiro dígito verificador
    # ==========================

    soma = 0
    peso = 10

    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = (soma * 10) % 11

    if resto == 10:
        digito1 = 0
    else:
        digito1 = resto

    if digito1 != int(cpf[9]):
        return False

    # ==========================
    # Segundo dígito verificador
    # ==========================

    soma = 0
    peso = 11

    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = (soma * 10) % 11

    if resto == 10:
        digito2 = 0
    else:
        digito2 = resto

    if digito2 != int(cpf[10]):
        return False

    return True