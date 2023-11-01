CREATE TABLE IF NOT EXISTS Jogo (
    N_Jogo INTEGER PRIMARY KEY ,
    estadio TEXT NOT NULL,
    time_visitante TEXT NOT NULL,
    time_mandante TEXT NOT NULL,
    placar_visitante INTEGER NOT NULL,
    placar_mandante INTEGER NOT NULL,
    N_rodada INTEGER NOT NULL,
    CHECK (time_visitante <> time_mandante)
);