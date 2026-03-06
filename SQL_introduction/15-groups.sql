-- Script qui affiche le nombre d'enregistrements
-- ayant le même score
-- Résultat trié par nombre d'enregistrements déissant

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
