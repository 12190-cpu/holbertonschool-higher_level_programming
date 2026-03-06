-- Script: 16-shows_by_genre.sql
-- Objectif: Lister tous les shows avec leurs genres.
-- Si un show n'a pas de genre, afficher NULL.
-- LEFT JOIN permet d'inclure les shows sans genre.

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
