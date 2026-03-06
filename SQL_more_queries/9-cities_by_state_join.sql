-- Script: 9-cities_by_state_join.sql
-- Objectif: Lister toutes les villes avec le nom de leur état.
-- On utilise un JOIN entre les tables cities et states.

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
