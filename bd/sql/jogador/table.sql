CREATE TABLE IF NOT EXISTS Jogador (
    bid INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    posicao INTEGER DEFAULT 0,
    numero_camisa INTEGER DEFAULT 0,
    nome_time TEXT,

    FOREIGN KEY(nome_time) REFERENCES Team(nome_time) ON DELETE CASCADE

);
