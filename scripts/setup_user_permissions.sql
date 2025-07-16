-- Script de configuration des permissions pour mohamed_dev
-- À exécuter après chaque restauration de base de données depuis la production

-- 1. Accorder l'usage du schéma public
GRANT USAGE ON SCHEMA public TO mohamed_dev;

-- 2. Accorder les permissions sur toutes les tables existantes
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO mohamed_dev;

-- 3. Accorder les permissions sur toutes les séquences existantes
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO mohamed_dev;

-- 4. Configurer les permissions par défaut pour les futurs objets
ALTER DEFAULT PRIVILEGES IN SCHEMA public 
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO mohamed_dev;

ALTER DEFAULT PRIVILEGES IN SCHEMA public 
    GRANT USAGE, SELECT ON SEQUENCES TO mohamed_dev;

-- 5. Vérifier que l'utilisateur peut accéder aux tables
-- (optionnel - pour debug)
-- SELECT table_name, privilege_type 
-- FROM information_schema.table_privileges 
-- WHERE grantee = 'mohamed_dev' AND table_schema = 'public'; 