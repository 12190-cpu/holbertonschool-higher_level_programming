-- Script: 5-unique_id.sql
-- Objectif: Créer la table unique_id
-- Le champ id doit être unique et possède une valeur par défaut de 1.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
