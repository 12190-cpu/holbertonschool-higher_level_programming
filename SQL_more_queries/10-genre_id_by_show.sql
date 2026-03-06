-- Script: 10-genre_id_by_show.sql
-- Objectif: Lister les shows ayant au moins un genre associé.
-- On utilise un INNER JOIN entre tv_shows et tv_show_genres.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
