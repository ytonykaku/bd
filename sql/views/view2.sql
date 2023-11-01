CREATE VIEW Camisa10Times AS
SELECT DISTINCT t.nome_time, j.nome AS nome_camisa10
FROM Team t
LEFT JOIN Jogador j ON t.nome_time = j.nome_time AND j.numero_camisa = 10;
