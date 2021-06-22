# https://docs.python.org/2/library/datetime.html
from datetime import datetime
from locale import LC_ALL, setlocale

from calendar import monthrange

dia_semana, ultimo_dia = monthrange(2020, 2)  # (ano, mês) - desempacota dia da semana e ultimo dia mes
print(ultimo_dia)  # Saída: 29 (último dia de fevereiro de 2020)

setlocale(LC_ALL, 'pt_BR.UTF-8')
data = datetime.now()
dt_format = data.strftime('%A, de %d de %B de %Y ')
print(dt_format)
