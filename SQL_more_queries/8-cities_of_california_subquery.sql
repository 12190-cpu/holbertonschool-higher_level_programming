-- Script: 8-cities_of_california_subquery.sql
-- Objectif: Lister les villes appartenant à l'état California
-- sans utiliser JOIN.
-- On utilise une sous-requête pour récupérer l'id de California.

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
