"""
Faça uma lista de tarefas com as seguintes opções:
adicionar tarefa
listar tarefa
opção de desfazer (a cada vez que chamarmos, desfaz a ultima ação)
opção de refazer (a cada vez que charmarmos, refaz a ultima ação)
['Tarefa 1', 'Tarefa 2']
['Tarefa 1'] <- Desfazer
['Tarefa 1', 'Tarefa 2']
"""


def desfaz_tarefa(lista_tarefa):
    lista_hist = lista_tarefa.pop()
    return lista_hist


def refaz_tarefa(lista_tarefa, lista_hist):
    lista_tarefa.append(lista_hist[-1])
    lista_hist.pop()


if __name__ == '__main__':
    lista_tarefa = []
    lista_hist = []

    while True:
        print('MENU')
        print('###################')
        print('Op -> 1 <- Criar Uma tarefa')
        print('Op -> 2 <- Desfazer tarefa')
        print('Op -> 3 <- Refazer tarefa')
        print('Op -> 4 <- Sair')

        op = input('Digite uma op: ')
        if op == '4':
            break
        elif op == '1':
            tarefa = input('Digite uma tarefa: ')
            lista_tarefa.append(tarefa)
        elif op == '2':
            desfazer = desfaz_tarefa(lista_tarefa)
            lista_hist.append(desfazer)

        elif op == '3':
            refaz_tarefa(lista_tarefa, lista_hist)
        else:
            print('Op invalida por favor digite outro numero!')
        print(lista_tarefa)
