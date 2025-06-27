import os
import sys

# Configuration de base du projet
project = 'Audioliz'
author = 'Audioliz Team'
release = '1.0'  # ou laisse vide si non versionné
html_show_sourcelink = False
html_title = "Audioliz Documentation"
html_short_title = "Audioliz"
html_theme = "furo"
# Configuration Read the Docs
if os.getenv("READTHEDOCS", None) == "True":
    html_output_dir = os.getenv("READTHEDOCS_OUTPUT", "_build")
    html_static_path = []  # Optionnel : vide pour éviter les erreurs
else:
    html_output_dir = "_build"

# Répertoire contenant les fichiers statiques (logos, CSS personnalisée, etc.)
html_static_path = ['../_static']
html_css_files = ['custom.css']
# Extensions Sphinx utilisées
extensions = ['sphinxcontrib.youtube']

# Configuration pour la langue par défaut
language = 'en'  # Changez en 'fr' pour la version française


