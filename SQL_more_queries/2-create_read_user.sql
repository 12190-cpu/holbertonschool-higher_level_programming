-- Script: 2-create_read_user.sql
-- Objectif:
-- 1. Créer la base de données hbtn_0d_2 si elle n'existe pas
-- 2. Créer l'utilisateur user_0d_2
-- 3. Donner uniquement le privilège SELECT sur cette base.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
