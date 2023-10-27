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

    create_script = (
        """
        CREATE TABLE IF NOT EXISTS Jogo (
    N_Jogo INTEGER PRIMARY KEY AUTOINCREMENT,
    estadio TEXT NOT NULL,
    time_visitante TEXT NOT NULL,
    time_mandante TEXT NOT NULL,
    placar_visitante INTEGER NOT NULL,
    placar_mandante INTEGER NOT NULL,
    N_rodada INTEGER NOT NULL,
)
        """,
        """ CREATE TABLE IF NOT EXISTS Gols (
    N_Jogo INTEGER NOT NULL,
    jogador_marcou INTEGER NOT NULL,
    jogador_assistencia INTEGER NOT NULL,
    time_marcou TEXT NOT NULL,
    time_sofreu TEXT NOT NULL,
    minuto INTEGER NOT NULL,

    FOREIGN KEY(N_Jogo) REFERENCES Jogo(N_Jogo) ON DELETE CASCADE
    FOREIGN KEY(jogador_marcou) REFERENCES Jogador(BID) ON DELETE CASCADE
    FOREIGN KEY(jogador_assistencia) REFERENCES Jogador(BID) ON DELETE CASCADE
    FOREIGN KEY(time_marcou) REFERENCES Team(nome_time) ON DELETE CASCADE
    FOREIGN KEY(time_sofreu) REFERENCES Team(nome_time) ON DELETE CASCADE
)
        """,
        """
        CREATE TABLE IF NOT EXISTS Faltas (
    N_Jogo INTEGER NOT NULL,
    jogador_recebeu INTEGER NOT NULL,
    jogador_marcou INTEGER NOT NULL,
    time_marcou TEXT NOT NULL,
    time_sofreu TEXT NOT NULL,
    minuto INTEGER NOT NULL,

    FOREIGN KEY(N_Jogo) REFERENCES Jogo(N_Jogo) ON DELETE CASCADE
    FOREIGN KEY(jogador_recebeu) REFERENCES Jogador(BID) ON DELETE CASCADE
    FOREIGN KEY(jogador_marcou) REFERENCES Jogador(BID) ON DELETE CASCADE
    FOREIGN KEY(time_marcou) REFERENCES Team(nome_time) ON DELETE CASCADE
    FOREIGN KEY(time_sofreu) REFERENCES Team(nome_time) ON DELETE CASCADE
)
        """,
        """
        CREATE TABLE IF NOT EXISTS Substituicoes (
    N_Jogo INTEGER NOT NULL,
    jogador_saiu INTEGER NOT NULL,
    jogador_entrou INTEGER NOT NULL,
    team  TEXT NOT NULL,
    minuto INTEGER NOT NULL,

    FOREIGN KEY(N_Jogo) REFERENCES Jogo(N_Jogo) ON DELETE CASCADE
    FOREIGN KEY(jogador_saiu) REFERENCES Jogador(BID) ON DELETE CASCADE
    FOREIGN KEY(jogador_entrou) REFERENCES Jogador(BID) ON DELETE CASCADE
    FOREIGN KEY(team) REFERENCES Team(nome_time) ON DELETE CASCADE

)
        """,
        """
        CREATE TABLE IF NOT EXISTS StatsTime (
nome_time TEXT PRIMARY KEY,
mando_de_campo TEXT PRIMARY KEY,
gols_marcados INTEGER DEFAULT 0,
gols_sofridos INTEGER DEFAULT 0,
vitorias INTEGER DEFAULT 0,
derrotas INTEGER DEFAULT 0,
empates INTEGER DEFAULT 0,
pontos INTEGER DEFAULT 0,
saldo_de_gols INTEGER DEFAULT 0,
num_jogos INTEGER DEFAULT 0,

FOREIGN KEY(nome_time) REFERENCES Team(nome_time) ON DELETE CASCADE
FOREIGN KEY(mando_de_campo) REFERENCES Team(nome_time) ON DELETE CASCADE

)
        """,
        """
        CREATE TABLE IF NOT EXISTS Team (
nome_time TEXT PRIMARY KEY,
SERIE CHAR NOT NULL,
UF VARCHAR(2) DEFAULT 0,
tecnico TEXT,

)
        """,
        """
        CREATE TABLE IF NOT EXISTS Jogador (
bid INTEGER PRIMARY KEY,
nome TEXT NOT NULL,
idade INTEGER NOT NULL,
posicao INTEGER DEFAULT 0,
numero_camisa INTEGER DEFAULT 0,
nome_time TEXT,

FOREIGN KEY(nome_time) REFERENCES Team(nome_time) ON DELETE CASCADE

)
        """,
        """CREATE TABLE IF NOT EXISTS Jogador (
        bid INTEGER PRIMARY KEY,
        faltas_sofridas INTEGER DEFAULT 0,
        faltas_feitas INTEGER DEFAULT 0,
        numero_de_gols INTEGER DEFAULT 0,
        amarelos INTEGER DEFAULT 0,
        vermelhos INTEGER DEFAULT 0,
        numero_de_assistencias INTEGER DEFAULT 0,


        FOREIGN KEY(bid) REFERENCES Team(bid) ON DELETE CASCADE

    )""")
    cur.execute(create_script)

    conn.commit()



except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
