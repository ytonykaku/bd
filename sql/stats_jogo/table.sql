CREATE TABLE IF NOT EXISTS StatsJogo (
    nome_time TEXT,
    N_Jogo INTEGER,
    cartao_amarelo INTEGER DEFAULT 0,
    cartao_vermelho INTEGER DEFAULT 0,
    impedimentos INTEGER DEFAULT 0,
    escanteios INTEGER DEFAULT 0,
    faltas INTEGER DEFAULT 0,
    passes INTEGER DEFAULT 0,
    chutes INTEGER DEFAULT 0,
    chutes_a_gol INTEGER DEFAULT 0,
    posse_de_bola INTEGER DEFAULT 0,
    precisao_do_passe INTEGER DEFAULT 0,

    PRIMARY KEY (nome_time, N_Jogo),
    FOREIGN KEY(N_Jogo) REFERENCES Jogo(N_Jogo) ON DELETE CASCADE
);

