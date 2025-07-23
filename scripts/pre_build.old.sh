#!/bin/bash

########## OLD ##########

# Détermine la langue depuis l'environnement
lang="${READTHEDOCS_LANGUAGE:-en}"

# Copie les fichiers .rst dans le répertoire racine
# Ils faut qu'ils soient là où se trouve conf.py

# la version anglaise
find documentation_content -name "*.rst" -type f -exec cp {} . \;
echo "Fichiers .rst de la version anglaise copiés récursivement"

# puis éventuellement une traduction
if [ "$lang" = "en" ]; then
    echo "Langue par défaut, aucune copie nécessaire."
else
    source_dir="locale/$lang"

    # Vérifier si le répertoire source existe
    if [ ! -d "$source_dir" ]; then
        echo "Erreur: Le répertoire de traduction $source_dir n'existe pas." >&2
        exit 1
    fi

    # Copie récursive du contenu
    cp -r "$source_dir"/* .
    echo "Contenu de $source_dir copié vers le répertoire courant."
fi

# Supprimer les occurrences de "|$|" dans tous les fichiers .rst
echo "Nettoyage des fichiers .rst..."
find . -name "*.rst" -type f | while read -r file; do
    sed -i 's/|$|//g' "$file"
    echo "Nettoyé : $file"
done 