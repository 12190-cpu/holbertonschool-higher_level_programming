-- Script qui affiche tous les enregistrements de second_table
-- où la colonne name contient une valeur
-- Affiche score puis name
-- Résultat trié par score décroissant

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
