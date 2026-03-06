-- Script: 1-create_user.sql
-- Objectif: Créer l'utilisateur user_0d_1 avec tous les privilèges
-- sur le serveur MySQL.
-- IF NOT EXISTS permet d'éviter une erreur si l'utilisateur existe déjà.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
