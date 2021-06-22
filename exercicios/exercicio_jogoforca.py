
print("** Bem-Vindo ao joguinho da forca, tente adivinhar a palavra secreta **")
palavra = input('Digite a palavra secreta: ')
print("\n" * 300)
digitado = []
tentativas = 5

while True:
    if tentativas > 0:
        letra = input(f'Tentativas restantes {tentativas}\n Digite uma letra: ')
    else:
        print(f'\nSuas tentativas acabaram você falhou a palavra era {palavra}')
        break

    if len(letra) > 1:
        print('\nOops! Você digitou mais de uma letra, tente novamente...')
        continue

    if letra in palavra:
        digitado.append(letra)
        print(f'\nParabéns! a letra {letra} existe na palavra secreta')
    else:
        tentativas -= 1
        print(f'\nA letra * {letra} * não existe na palavra - Restam {tentativas} tentativas')

    letra_temp = ''
    for letra_palavra in palavra:
        if letra_palavra in digitado:
            letra_temp += letra_palavra
        else:
            letra_temp += '*'

    if letra_temp == palavra:
        print(f'\nPARABÉNS! VOCÊ CONSEGUIU A PALAVRA ERA {palavra}')
        break
    else:
        print(f'\nA palavra está assim: {letra_temp}')


