-- Script: 6-states.sql
-- Objectif:
-- 1. Créer la base hbtn_0d_usa
-- 2. Créer la table states avec un id auto-incrémenté
-- servant de clé primaire.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
