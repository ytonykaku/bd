CREATE TABLE IF NOT EXISTS Team (
    nome_time TEXT PRIMARY KEY,
    serie CHAR NOT NULL,
    UF VARCHAR(2),
    tecnico TEXT UNIQUE,

    FOREIGN KEY (UF) REFERENCES EstadosBrasil (UF)
);
