CREATE VIEW MediaFaltasJogadores AS
SELECT AVG(sj.faltas_feitas) AS media_faltas
FROM StatsJogador sj;