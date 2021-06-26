#DESAFIO VALIDAR DIGITO CPF

cpf = input("Digite um cpf no formato ###.###.###-## ")
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
cpf_format = cpf[:-2]
total = 0
index = 0
reverso = 10
calcula_digito = 0
digito_1 = ''
digito_2 = ''

while digito_2 == '':
    if reverso >= 2:
        total += reverso * int(cpf_format[index])
        index += 1
        reverso -= 1
    else:
        calcula_digito = (11 - (total % 11))
        if digito_1 == '':
            if calcula_digito > 9:
                digito_1 = 0
            else:
                digito_1 = calcula_digito

            cpf_format += str(digito_1)

            index = 0
            reverso = 11
            total = 0

        else:
            if calcula_digito > 9:
                digito_2 = 0
            else:
                digito_2 = calcula_digito

            cpf_format += str(digito_2)

if cpf_format == cpf:
    print("CPF validado com sucesso!")
else:
    print("CPF invalido verifique os numeros digitados.")







