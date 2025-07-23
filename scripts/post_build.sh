#!/bin/bash

# # Définir les répertoires à exclure
# excluded_dirs=(
#     "documentation_main"
#     "documentation_clients"
#     "locale"
# )

# # Construire la chaîne d'exclusion pour find
# exclude_pattern=""
# for dir in "${excluded_dirs[@]}"; do
#     exclude_pattern="$exclude_pattern -not -path './$dir/*'"
# done

# # Supprimer les fichiers .rst en excluant les répertoires spécifiés
# echo "Nettoyage des fichiers .rst temporaires..."
# eval "find . -name '*.rst' -type f $exclude_pattern -exec rm {} \;"
# echo "Fichiers .rst temporaires supprimés."

rm -f index.rst
rm -rf howtos/
rm -rf reference/
rm -rf client/


