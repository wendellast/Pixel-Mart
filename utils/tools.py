import re


def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r"[^0-9]", "", cpf)

    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False

def valida_cep(cep):
    cep = str(cep)
    cep = re.sub(r"[^0-9]", "", cep)

    if not cep or len(cep) != 8:
        return False
    else:
        return True

def price_format(value):
    return f"R$ {value:.2f} ".replace(".", ",")
