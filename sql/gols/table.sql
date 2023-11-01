CREATE TABLE IF NOT EXISTS Gols (
    N_Jogo INTEGER NOT NULL,
    jogador_marcou INTEGER NOT NULL,
    jogador_assistencia INTEGER NOT NULL,
    time_marcou TEXT NOT NULL,
    time_sofreu TEXT NOT NULL,
    minuto INTEGER NOT NULL,
    segundo INTEGER NOT NULL,
    CHECK (segundo >= 0 AND segundo < 60 ),
    CHECK (time_marcou <> time_sofreu),

    FOREIGN KEY (N_Jogo) REFERENCES Jogo(N_Jogo) ON DELETE CASCADE,
    FOREIGN KEY (jogador_marcou) REFERENCES Jogador(bid) ON DELETE CASCADE,
    FOREIGN KEY (jogador_assistencia) REFERENCES Jogador(bid) ON DELETE CASCADE,
    FOREIGN KEY (time_marcou) REFERENCES Team(nome_time) ON DELETE CASCADE,
    FOREIGN KEY (time_sofreu) REFERENCES Team(nome_time) ON DELETE CASCADE
);
