import os
import sys

# Configuration de base du projet
project = 'Audioliz'
author = 'Audioliz Team'
release = '1.0'  # ou laisse vide si non versionné
html_show_sourcelink = False
# html_theme = "furo"
html_theme = "sphinx_rtd_theme"

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

# Exclure les fichiers de packages installés de la traduction
gettext_allow_fuzzy_translations = True
gettext_location = False
gettext_compact = False

# Configuration spécifique pour gettext
gettext_auto_build = False  # Éviter la génération automatique
gettext_additional_targets = []  # Pas de cibles supplémentaires

# Configuration pour éviter le traitement des environnements virtuels
gettext_ignore_patterns = [
    '**/.venv/**',
    '**/.env/**',
    '**/venv/**',
    '**/env/**',
    '**/site-packages/**',
    '**/dist-info/**',
    '**/__pycache__/**',
]

# Configuration pour exclure les environnements virtuels de la génération des .pot
gettext_exclude_patterns = [
    '**/.venv/**',
    '**/.env/**',
    '**/venv/**',
    '**/env/**',
    '**/site-packages/**',
    '**/dist-info/**',
    '**/__pycache__/**',
    '**/node_modules/**',
]

# Exclure les fichiers de templates d'autosummary
exclude_patterns = [
    '**/site-packages/**',
    '**/dist-info/**',
    '**/autosummary/templates/**',
    '**/.*/**',  # Ignorer tous les dossiers commençant par .
    '**/_build/**',  # Ignorer spécifiquement le dossier _build
    '**/_templates/**',  # Ignorer les templates personnalisés si présents
    '**/_cache/**',  # Ignorer les caches si présents
    '**/.env/**',  # Ignorer l'environnement virtuel .env
    '**/.venv/**',  # Ignorer l'environnement virtuel .venv
    '**/venv/**',  # Ignorer l'environnement virtuel venv
    '**/env/**',  # Ignorer l'environnement virtuel env
    '**/node_modules/**',  # Ignorer node_modules si présent
    '**/__pycache__/**',  # Ignorer les caches Python
    '**/*.pyc',  # Ignorer les fichiers Python compilés
    '**/locale/**/.venv/**',  # Ignorer spécifiquement .venv dans locale
    '**/locale/**/.*/**',  # Ignorer tous les dossiers cachés dans locale
]

# configuration pour le theme sphinx_rtd_theme
html_theme_options = {
    'language_selector': True,
    'version_selector': False,
    'flyout_display': False,
}

# Configuration multilingue pour Read the Docs
if os.getenv("READTHEDOCS", None) == "True":
    # Récupération de la langue depuis l'environnement Read the Docs
    language = os.getenv("READTHEDOCS_LANGUAGE", "fr")

# Configuration des tags pour les spécificités client
# utilisés par sphinx 
tags = []

# Détection automatique de l'environnement client
version = os.getenv("READTHEDOCS_VERSION_NAME", "local")
if version and version not in ["main", "dev"]:
    tags.append(version)
    client_name = version.capitalize()
    html_title = f"Audioliz Documentation for {client_name}"
    html_short_title = f"Audioliz for {client_name}"

    # Configuration des variables de substitution
    rst_epilog = f"""
    .. |html_title| replace:: {html_title}
    .. |client_name| replace:: {client_name}
    """
else:
    client_name = ""
    html_title = "Audioliz Documentation"
    html_short_title = "Documentation"


