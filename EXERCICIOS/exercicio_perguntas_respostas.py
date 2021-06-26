perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2*3 ? ',
        'respostas': {'a': '6', 'b': '4', 'c': '10', },
        'resposta_certa': 'a',
    },
}
print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print()
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_user = input('Insira a reposta: ')

    if resposta_user == pv['resposta_certa']:
        print('Parabéns você acertou! ')
        respostas_certas += 1
    else:
        print('Que pena você errou...')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} e sua taxa de acerto foi de {porcentagem_acerto}%')