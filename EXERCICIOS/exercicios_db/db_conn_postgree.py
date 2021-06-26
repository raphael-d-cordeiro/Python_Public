import psycopg2
from contextlib import contextmanager


@contextmanager
def conn():
    _connect_db = psycopg2.connect(
        host='',
        database='',
        user='',
        password=''
    )
    try:
        yield _connect_db
    finally:
        _connect_db.close()


def query_db(param=None):
    s = """
             SELECT TO_CHAR(ARQATEND.DATATEND,'DD/MM/YYYY') DATAATENDIMENTO
              , TO_CHAR(ARQATEND.DATACAD,'DD/MM/YYYY') DATACAD
              , CADESPCI.DESCRESPCI	ESPECIALIDADE
              , ARQATEND.NUMATEND	ATENDIMENTO
              , ARQATEND.CIDPRIN	CID
              , ARQATEND.PROCPRIN	PROCPRIN
              , CADSERV.CODSERV		SERVICO
              , CADSERV.NOMESERV    NOMESERVICO
              , CADPAC.NOMEPAC		PACIENTE
              , CADPREST.NOMEPREST	MEDICO
              , CADCONV.NOMECONV	CONVENIO
              , CADPLACO.NOMEPLACO	PLANO
              , CONTAS.*
           FROM ARQATEND
           LEFT JOIN CADPLACO		ON ARQATEND.CODPLACO = CADPLACO.CODPLACO
           LEFT JOIN ARQCIR			ON ARQATEND.NUMATEND = ARQCIR.NUMATEND
           LEFT JOIN CADCIR			ON ARQCIR.CODCIR     = CADCIR.CODCIR 
           LEFT JOIN CADESPCI		ON CADCIR.CODESPCIR  = CADESPCI.CODESPCI
           LEFT JOIN CADCONV		ON CADPLACO.CODCONV  = CADCONV.CODCONV      
           LEFT JOIN CADPAC			ON ARQATEND.CODPAC   = CADPAC.CODPAC
           LEFT JOIN CADSERV		ON ARQATEND.CODSERV  = CADSERV.CODSERV
           LEFT JOIN CADPREST		ON ARQATEND.CODPREST = CADPREST.CODPREST
           LEFT JOIN CONTAS			ON ARQATEND.NUMATEND = CONTAS.NUMATEND
          WHERE ARQATEND.DATATEND BETWEEN '2015-01-01 00:00:00' AND '2020-02-28 23:59:59'AND
          CADPAC.NOMEPAC LIKE '{}'         
        """.format(param)

    with conn() as connect_db:
        with connect_db.cursor() as cur:
            cur.execute(s)
            colum_names = [desc[0] for desc in cur.description]
            rs = cur.fetchall()
            """if you prefer, you can export to csv file"""
            # with open('prontuario.csv', 'w') as arq_csv:
            #     cur.copy_expert("COPY ({0}) TO STDOUT WITH CSV HEADER".format(s), arq_csv)
            return colum_names, rs


if __name__ == '__main__':
    result = query_db(param="""%PERSON NAME%""")
    print(result)
