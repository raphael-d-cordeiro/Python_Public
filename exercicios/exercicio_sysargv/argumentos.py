import sys, os

argumentos = sys.argv

qtd_args = len(argumentos)

if qtd_args <= 1:
    print('Favor enviar os argumentos')
    print('-a', 'Para listar todos os arquivos nesta pasta', sep='\t')
    print('-b', 'Para listar todos os diretórios nesta pasta', sep='\t')
    sys.exit()

for file in os.listdir('.'):
    if '-a' in argumentos:
        if os.path.isfile(file):
            print(file)
    elif '-b' in argumentos:
        if os.path.isdir(file):
            print(file)

