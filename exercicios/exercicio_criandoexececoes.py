class BugouError(Exception):
    pass

def testar():
    raise BugouError("Tudo bugado")

try:
    testar()
except BugouError as error:
    print(f'Este é o erro: {error}')