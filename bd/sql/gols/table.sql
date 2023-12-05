CREATE TABLE IF NOT EXISTS Gols (
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
);
