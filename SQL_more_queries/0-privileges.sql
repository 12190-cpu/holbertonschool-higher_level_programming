-- Script: 0-privileges.sql
-- Objectif: Afficher tous les privilèges des utilisateurs
-- user_0d_1 et user_0d_2 sur le serveur MySQL local.
-- La commande SHOW GRANTS permet de voir les droits attribués
-- à un utilisateur spécifique.

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
