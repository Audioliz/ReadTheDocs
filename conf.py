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
html_static_path = ['_static']
# html_css_files = ['custom.css']
# html_js_files = ['language-selector.js']

# Extensions Sphinx utilisées
extensions = [
    'sphinxcontrib.youtube',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

# Configuration pour l'internationalisation
language = 'en'  # Langue par défaut
locale_dirs = ['locale']        # où sont vos .po/.mo
gettext_uuid = True             # pour des .pot stables
gettext_compact = False

html_theme_options = {
    'language_selector': True,
}

# Configuration multilingue pour Read the Docs
if os.getenv("READTHEDOCS", None) == "True":
    # Récupération de la langue depuis l'environnement Read the Docs
    language = os.getenv("READTHEDOCS_LANGUAGE", "fr")
    
    # Configuration des langues supportées
    html_theme_options.update({
        'language_versions': {
            'en': 'English',
            'fr': 'Français',
        }
    }
else:
    # Configuration locale pour le développement
    html_theme_options.update({
        'language_versions': {
            'en': 'English',
            'fr': 'Français',
        }
    }

# Configuration pour Weblate
gettext_allow_fuzzy_translations = True



