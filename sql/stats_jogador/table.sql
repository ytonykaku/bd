CREATE TABLE IF NOT EXISTS Jogador (
    bid INTEGER PRIMARY KEY,
    faltas_sofridas INTEGER DEFAULT 0,
    faltas_feitas INTEGER DEFAULT 0,
    numero_de_gols INTEGER DEFAULT 0,
    amarelos INTEGER DEFAULT 0,
    vermelhos INTEGER DEFAULT 0,
    numero_de_assistencias INTEGER DEFAULT 0,


    FOREIGN KEY(bid) REFERENCES Team(bid) ON DELETE CASCADE

);
