import re
import random

VALIDADOR = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida_cnpj(cnpj):
    cnpj_formatado = formata_cnpj(cnpj)
    cnpj_formatado = calcula_digito(cnpj_formatado, 1)
    cnpj_completo = calcula_digito(cnpj_formatado, 2)
    cnpj_validado = '{}.{}.{}/{}-{}'.format(cnpj_completo[:2], cnpj_completo[2:5],
                                            cnpj_completo[5:8], cnpj_completo[8:12],
                                            cnpj_completo[12:14])
    if cnpj == cnpj_validado:
        return f'{cnpj} - CNPJ validado com sucesso!'
    else:
        return f'{cnpj} - CNPJ invalido, verifique o numero informado!'


def gera_cnpj():
    primeiro_bloco = random.randint(00, 99)
    segundo_bloco = random.randint(000, 999)
    terceiro_bloco = random.randint(000, 999)
    quarto_bloco = '0001'
    novo_cnpj = f'{primeiro_bloco}{segundo_bloco}' \
                f'{terceiro_bloco}{quarto_bloco}'

    novo_cnpj = calcula_digito(novo_cnpj, 1)
    novo_cnpj = calcula_digito(novo_cnpj, 2)
    return novo_cnpj


def formata_cnpj(cnpj):
    cnpj_formatado = re.sub(r'[^0-9]', '', cnpj)
    return cnpj_formatado[0:12]


def calcula_digito(cnpj, digito):
    total = 0
    valida_dig = []
    if digito == 1:
        valida_dig = VALIDADOR[1:]
    elif digito == 2:
        valida_dig = VALIDADOR

    for i, v in enumerate(valida_dig):
        total += int(cnpj[i]) * v

    dig_resul = 11 - (total % 11)
    if dig_resul > 9:
        dig_resul = 0
    return cnpj + str(dig_resul)
