from dados_map import produtos, pessoas, lista
from functools import reduce


# acumula = 0
# for item in lista:
#     acumula += item
#
# print(acumula)

# soma_lista = reduce(lambda ac, item: item + ac, lista, 0)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos / len(produtos))

soma_idades = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_idades / len(pessoas))

