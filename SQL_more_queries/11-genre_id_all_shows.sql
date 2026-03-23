-- Script: 11-genre_id_all_shows.sql
-- Objectif: Lister tous les shows même ceux sans genre.
-- LEFT JOIN permet d'afficher NULL lorsqu'il n'y a pas de genre.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
