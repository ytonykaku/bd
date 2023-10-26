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

);
