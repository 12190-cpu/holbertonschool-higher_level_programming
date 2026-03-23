-- Script: 13-count_shows_by_genre.sql
-- Objectif: Compter le nombre de shows par genre.
-- GROUP BY permet de regrouper les shows par genre.

SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
