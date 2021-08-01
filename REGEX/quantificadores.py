#Meta caracteres ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
#{min. max}
#{10,} 10 ou mais
#{,10} de zero a 10
#{5,10} de 5 a 10
# (grupo)+ [a-zA-Z]+
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos ○atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
Jã
'''

print(re.findall(r'jO+ãO+', texto, flags=re.I))
print(re.sub(r'jO+ãO+', 'Raphael', texto, flags=re.I))
print(re.sub(r'jO?ãO*', 'Raphael', texto, flags=re.I))
print(re.findall(r'jO{1,}ãO{1,}', texto, flags=re.I))
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
