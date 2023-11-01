CREATE VIEW TimesSemGols AS
SELECT DISTINCT t.nome_time
FROM Team t
LEFT JOIN Jogo j ON t.nome_time = j.time_mandante OR t.nome_time = j.time_visitante
WHERE NOT EXISTS (
    SELECT 1
    FROM Gols g
    WHERE g.N_Jogo = j.N_Jogo
);
