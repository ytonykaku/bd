import psycopg2

hostname = 'localhost'
database = 'campeonatobrasileiro'
username = 'postgres'
pwd = 'admin'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)

    cur = conn.cursor()

    create_script = '''CREATE TABLE IF NOT EXISTS Jogador (
    bid INTEGER PRIMARY KEY,
    faltas_sofridas INTEGER DEFAULT 0,
    faltas_feitas INTEGER DEFAULT 0,
    numero_de_gols INTEGER DEFAULT 0,
    amarelos INTEGER DEFAULT 0,
    vermelhos INTEGER DEFAULT 0,
    numero_de_assistencias INTEGER DEFAULT 0,


    FOREIGN KEY(bid) REFERENCES Team(bid) ON DELETE CASCADE

)'''
    cur.execute(create_script)
    
    conn.commit()



except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
