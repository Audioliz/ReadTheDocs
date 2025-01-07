import os

# Configurer la sortie correcte pour Read the Docs
if os.getenv("READTHEDOCS", None) == "True":
    html_output_dir = os.getenv("READTHEDOCS_OUTPUT", "_build")
    html_static_path = []  # Optionnel si Read the Docs génère des erreurs sur les fichiers statiques
else:
    html_output_dir = "_build"

# Répertoire de sortie HTML
html_static_path = ['static']
