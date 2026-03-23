-- Script: 4-never_empty.sql
-- Objectif: Créer la table id_not_null
-- Le champ id possède une valeur par défaut de 1
-- si aucune valeur n'est fournie lors de l'insertion.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
