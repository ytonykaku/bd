CREATE VIEW TimesSemGols AS
SELECT nome_time
FROM StatsTime
WHERE gols_sofridos = 0;