import os

caminho_pesquisa = input('Digite um caminho: ')
termo_pesquisa = input('Digite um termo para pequisa: ')

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'


conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_pesquisa):
    for arquivo in arquivos:
        if termo_pesquisa in arquivo:
            try:
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Arquivo Localizado!')
                print(f'{arquivo}')
                print(f'Caminho: {caminho_completo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {ext_arquivo}')
                print(f'Tamanho: {formata_tamanho(tamanho)}')
                conta += 1
            except PermissionError as e:
                print('Sem permissão na pasta.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado!')
            except Exception as e:
                print('Erro desconhecido.', e)
print()
print(f'{conta} arquivos encontrados.')