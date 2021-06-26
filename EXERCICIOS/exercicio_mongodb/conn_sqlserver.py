# pip install py odbc
import pyodbc

server = 'DESKTOP-O4NB2L0\SQLEXPRESS'
database = 'Estudo_MongoDB'
username = 'aula_mongodb'
password = 'abc123'

# for database user conn
string_conn = 'DRIVER={SQL Server Native Client 11.0};'
string_conn += f'SERVER={server};DATABASE={database};UID={username};PWD={password}'

# for windows user conn
#string_conn = 'DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;'

conexao = pyodbc.connect(string_conn)
cursor = conexao.cursor()

cursor.execute("Select * from Tbl_Teste")

for row in cursor:
    print(row)

cursor.close()
conexao.close()
