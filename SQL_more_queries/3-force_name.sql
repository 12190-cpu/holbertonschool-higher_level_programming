-- Script: 3-force_name.sql
-- Objectif: Créer la table force_name
-- Le champ name ne peut pas être NULL grâce à la contrainte NOT NULL.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
