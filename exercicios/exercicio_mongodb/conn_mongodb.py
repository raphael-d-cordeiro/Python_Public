# https://pymongo.readthedocs.io/en/stable/tutorial.html
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)

# Criando Base de Dados
db = client.Estudo_MongoDB



# Inserindo Dados

# db.pessoas.insert_one({
#     "id":1,
#     "nome": "James",
#     "idade": 45,
# })

# db.pessoas.insert_one({
#     "id":1,
#     "nome": "James",
#     "idade": 45,
#     "filhos": ["Jose", "Schneider", 45]
# })

# db.pessoas.insert_many([
#     {
#         "id": 4,
#         "nome": "Charlies",
#         "idade": 45,
#         "filhos": ["Jose", "Schneider", 45]
#     },
#     {
#         "id": 2,
#         "nome": "Amarildo",
#         "idade": 45,
#         "filhos": ["Jose", "Schneider", 45]
#     },
#     {
#         "id": 3,
#         "nome": "Chaves",
#         "idade": 45,
#         "filhos": ["Jose", "Schneider", 45]
#     },
# ])
# print(db.list_collection_names())
# print(db.pessoas.find_one())
#
# print(db.pessoas.find_one({"idade": 45}))

# localizados = db.pessoas.find_one({"idade": 45})
#
# for k, v in localizados.items():
#     print(k, v)

localizados = db.pessoas.find({"idade": 45})

# find retorna um dicionario de dados
for v in localizados:
    for k, p in v.items():
        print(k, p)

