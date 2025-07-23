#!/usr/bin/env python3
"""
Script de préparation pour la construction de la documentation.
Copie et nettoie les fichiers .rst.
"""

import os
import sys
import shutil
import glob
from pathlib import Path
import re

# Codes ANSI pour la coloration
RED = '\033[91m'
RESET = '\033[0m'

clients_map = {
    "latest": 0, # main documentation. Not client specific.
    "bruneau": 3,
    "wonderbox": 7,
    "audioliz": 52,
}

# Détermine la langue et la version depuis l'environnement
lang = os.environ.get("READTHEDOCS_LANGUAGE", "en")
version = os.environ.get("READTHEDOCS_VERSION", "latest")
print(f"Langue détectée: {lang}")
print(f"Version détectée: {version}")
client_id = clients_map.get(version, clients_map["latest"])
print(f"Client ID détecté: {client_id}")

def main():
    
    # Liste des répertoires sources et destinations
    source_dest_dirs = []
    
    # Ddocumentation principale
    source_dest_dirs.append(["documentation_main", "."])

    # Ddocumentation du client
    if client_id:
        source_dest_dirs.append([f"documentation_clients/{version}", "client"])

    # Ajouter ENSUITE les répertoires des traductions si nécessaire
    if lang != "en":
        source_dest_dirs.append([f"locale/{lang}/documentation_main", "."])
        if client_id:
            source_dest_dirs.append([f"locale/{lang}/documentation_clients/{version}", "client"])

    
    # Copie et nettoie récursivement chaque répertoire source
    print("Copie récursive des répertoires...")
    for source_dir, dest_dir in source_dest_dirs:
        copy_and_clean_recursively(source_dir, dest_dir)
    print("Copie terminée.")

    # # ajoute index_addendum.rst à l'index principal
    # if client_id != 0:
    #     # Check if client/index_addendum.rst exists
    #     addendum_path = os.path.join("client", "index_addendum.rst")
    #     if not os.path.exists(addendum_path):
    #         print(f"Warning: {addendum_path} not found - skipping index addendum")
    #     else:
    #         # Read content of index_addendum.rst
    #         with open(addendum_path, 'r', encoding='utf-8') as f:
    #             addendum_content = f.read()
            
    #         # Append to index.rst
    #         with open("index.rst", 'a', encoding='utf-8') as f:
    #             f.write("\n")  # Add blank line before appending
    #             f.write(addendum_content)
    #         print(f"Added content from {addendum_path} to index.rst")



def copy_and_clean_recursively(source_dir, dest_dir):
    """Copie récursivement un répertoire en préservant l'arborescence et nettoie les fichiers .rst."""
    try:
        # Vérifier si le répertoire source existe
        if not os.path.exists(source_dir):
            print(f"{RED}Le répertoire source {source_dir} n'existe pas - ignoré{RESET}")
            return
            
        # Créer le répertoire de destination s'il n'existe pas
        os.makedirs(dest_dir, exist_ok=True)
        
        # Copie et nettoie tout le contenu du répertoire source vers le répertoire destination
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            dest_item = os.path.join(dest_dir, item)
            
            if os.path.isdir(source_item):
                # Copier le répertoire récursivement en forçant l'écrasement
                shutil.copytree(source_item, dest_item, dirs_exist_ok=True)
                print(f"Copié: {source_item} -> {dest_item}")
                
                # Nettoyer les fichiers .rst dans le répertoire copié
                clean_rst_files_in_directory(dest_item)
            else:
                # Copier le fichier
                shutil.copy2(source_item, dest_item)
                print(f"Copié: {source_item} -> {dest_item}")
                
                # Nettoyer le fichier .rst s'il en est un
                if dest_item.endswith('.rst'):
                    clean_rst_file(dest_item)
            
    except Exception as e:
        print(f"{RED}Erreur lors de la copie de {source_dir} vers {dest_dir}: {e}{RESET}")


def clean_rst_files_in_directory(directory):
    """Nettoie tous les fichiers .rst dans un répertoire et ses sous-répertoires."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.rst'):
                file_path = os.path.join(root, file)
                clean_rst_file(file_path)


def clean_rst_file(file_path):
    """Nettoie un fichier .rst en supprimant les occurrences de '|$|'."""
    try:
        # Lit le contenu du fichier
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Keep content between client_id tags, remove content between other client tags (ex : |52|Spécifique pour Audioliz|52|)
        pattern = rf"\|(?!{client_id}\|)(\d+)\|.*?\|\1\|"
        cleaned_content = re.sub(pattern, "", content)
        # Remove client_id tags
        cleaned_content = re.sub(r"\|\d+\|", "", cleaned_content)
        # Supprime les occurrences de "|$|"
        cleaned_content = cleaned_content.replace("|$|", "")
        
        # Écrit le contenu nettoyé
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"  Nettoyé : {file_path}")
    except Exception as e:
        print(f"{RED}Erreur lors du nettoyage de {file_path}: {e}{RESET}")


if __name__ == "__main__":
    main() 