CREATE VIEW JogadorMaisFaltas AS
SELECT j.bid, j.nome, j.idade, j.posicao, j.numero_camisa, j.nome_time, sj.faltas_feitas AS faltas_mais
FROM Jogador j
INNER JOIN StatsJogador sj ON j.bid = sj.bid
WHERE sj.faltas_feitas = (SELECT MAX(faltas_feitas) FROM StatsJogador);