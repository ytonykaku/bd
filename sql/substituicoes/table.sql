CREATE TABLE IF NOT EXISTS Substituicoes (
    N_Jogo INTEGER NOT NULL,
    jogador_saiu INTEGER NOT NULL,
    jogador_entrou INTEGER NOT NULL,
    team  TEXT NOT NULL,
    minuto INTEGER NOT NULL,

    FOREIGN KEY(N_Jogo) REFERENCES Jogo(N_Jogo) ON DELETE CASCADE,
    FOREIGN KEY(jogador_saiu) REFERENCES Jogador(bid) ON DELETE CASCADE,
    FOREIGN KEY(jogador_entrou) REFERENCES Jogador(bid) ON DELETE CASCADE,
    FOREIGN KEY(team) REFERENCES Team(nome_time) ON DELETE CASCADE
);