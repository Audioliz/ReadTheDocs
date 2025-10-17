#!/usr/bin/env python3

import os
import json
import hashlib
import sys
from openai import OpenAI
from pathlib import Path

"""
Execute the script from the root of the project.

This script is used to translate the RST files.
It uses the OpenAI API to translate the files.
It uses a cache to avoid translating the same file twice.
It uses a dry run to avoid actually translating the files.
It uses a maximum number of files to translate to avoid translating too many files.
"""

# 📌 Configuration
LANGUAGES = ["fr"]
ROOT_DIR = Path("")
TARGET_BASE = Path("locale")
MODEL = "gpt-4"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
CACHE_FILE = Path(".rst-translation-cache.json")
DRY_RUN = False  # ⬅️ Active le mode simulation ici
MAX_NB_FILES_TRANSLATED = 50  # Augmenté pour l'automatisation

# # list of directories to translate : ROOT_DIR -> target_dir (relative to <TARGET_BASE>/<lang>/)
# location_map = {
#     "documentation_main": "main",
#     "documentation_clients": "clients",
# }

# 
def format_specific_files(specific_files):

    files_to_process = []
    for file_arg in specific_files:
        file_path = Path(file_arg)
        # if not file_path.is_absolute():
        #     file_path = ROOT_DIR / file_path
        if file_path.exists() and file_path.suffix == ".rst":
            files_to_process.append(file_path)
        else:
            print(f"⚠️  Fichier ignoré (n'existe pas ou n'est pas un .rst) : {file_arg}")

    return files_to_process

# 🔐 Fonction pour calculer le hash du contenu
def compute_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

# 📦 Charger ou initialiser le cache
def load_cache():
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"⚠️  Erreur de format JSON dans le cache : {e}")
            print("🔄 Recréation du cache...")
            # Sauvegarder l'ancien cache corrompu
            backup_file = CACHE_FILE.with_suffix('.json.backup')
            CACHE_FILE.rename(backup_file)
            print(f"💾 Ancien cache sauvegardé dans : {backup_file}")
            return {}
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2)

# 🤖 Appel OpenAI pour la traduction
def translate_rst_file(content: str, target_lang: str) -> str:
    prompt = f"""Tu es un traducteur professionnel spécialisé dans la documentation technique Sphinx (.rst).
Garde exactement la structure du document, les blocs de code, les titres, les liens, les directives (comme .. image::), etc.
Ne modifie rien d'autre que la langue du texte courant.
En particulier, ne modifie pas les lignes qui suivent la directive ..toctree::
Par exemple si tu vois :
""
.. toctree::
   :caption: Main documentation
   :maxdepth: 2

   intro
   strings
   datatypes
   numeric
""
Tu dois traduire seulement :caption.
""
.. toctree::
   :caption: Main documentation
   :maxdepth: 2

   intro          <<< ne pas traduire
   strings        <<< ne pas traduire
   datatypes      <<< ne pas traduire
   numeric        <<< ne pas traduire
""
Toutes les parties délimitées par "|$|" ne doivent pas être traduites. Exemple :
"My name is|$|Mad Dog|$|" doit être traduit en "Mon nom est|$|Mad Dog|$|".

IMPORTANT : Ta réponse doit être le contenu RST traduit directement, sans backticks ni balises de code.
Ne pas inclure ```rst au début ni ``` à la fin de ta réponse.

Traduis ce document en {target_lang.upper()} :

{content}"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Tu es un assistant expert en traduction technique. Tu réponds toujours avec le contenu RST pur, sans balises de code."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

# def process_rst_file(source: Path, dest_dir: Path, lang: str, cache: dict = None, force_translation: bool = False) -> dict:
#     """
#     Translate a single RST file to the specified language.
    
#     Args:
#         source: Path to the source RST file
#         dest_dir: Base directory for translated files
#         lang: Target language code
#         cache: Optional cache dictionary for tracking file changes
#         force_translation: Whether to force translation even if file hasn't changed
    
#     Returns:
#         dict: Result information with keys:
#             - success: bool indicating if translation was successful
#             - translated: bool indicating if file was actually translated
#             - output_path: Path to the translated file (if successful)
#             - error: error message (if failed)
#     """
#     result = {
#         "success": False,
#         "translated": False,
#         "output_path": None,
#         "error": None
#     }
    
#     try:
#         # Read source file
#         with open(source, "r", encoding="utf-8") as f:
#             original_content = f.read()
        
#         original_hash = compute_hash(original_content)
#         relative_path = source.relative_to(ROOT_DIR)
#         output_path = dest_dir / lang / relative_path
        
#         # Check if translation is needed
#         if cache is not None:
#             cache_key = f"{lang}:{str(source)}"
#             previous_hash = cache.get(cache_key)
            
#             if previous_hash == original_hash and output_path.exists() and not force_translation:
#                 result["success"] = True
#                 result["translated"] = False
#                 result["output_path"] = output_path
#                 return result
        
#         # Perform translation
#         translated = translate_rst_file(original_content, lang)
        
#         # Create output directory and save translated file
#         output_path.parent.mkdir(parents=True, exist_ok=True)
#         with open(output_path, "w", encoding="utf-8") as f:
#             f.write(translated)
        
#         # Update cache if provided
#         if cache is not None:
#             cache_key = f"{lang}:{str(source)}"
#             cache[cache_key] = original_hash
        
#         result["success"] = True
#         result["translated"] = True
#         result["output_path"] = output_path
        
#     except Exception as e:
#         result["error"] = str(e)
    
#     return result

def process_rst_files(files, force=False):
    cache = load_cache()
    updated = False
    nb_files_translated = 0

    for filepath in files:
        if nb_files_translated >= MAX_NB_FILES_TRANSLATED and not DRY_RUN:
            break

        with open(filepath, "r", encoding="utf-8") as f:
            original_content = f.read()

        original_hash = compute_hash(original_content)

        for lang in LANGUAGES:
            cache_key = f"{lang}:{str(filepath)}"
            previous_hash = cache.get(cache_key)
            relative_path = filepath.relative_to(ROOT_DIR)
            output_path = TARGET_BASE / lang / relative_path

            if previous_hash == original_hash and output_path.exists() and not force:
                print(f"⏩ Pas de changement pour {filepath} ({lang})")
                continue

            if DRY_RUN:
                print(f"🔍 DRY RUN : À traduire → {filepath} ({lang})")
                continue

            print(f"🌍 Traduction de {filepath} en {lang}...")
            try:
                translated = translate_rst_file(original_content, lang)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(translated)
                cache[cache_key] = original_hash
                updated = True
                print(f"✅ Sauvegardé : {output_path}")
                nb_files_translated += 1
            except Exception as e:
                print(f"❌ Erreur traduction {filepath} ({lang}) : {e}")

    if not DRY_RUN and updated:
        save_cache(cache)
        print("💾 Cache mis à jour.")

def main():
    
    # Récupérer les arguments de ligne de commande (fichiers spécifiques à traduire)
    specific_files = sys.argv[1:] if len(sys.argv) > 1 else None
    
    if specific_files:
        print(f"🎯 Traduction des fichiers spécifiés : {specific_files}")
        process_rst_files(files=format_specific_files(specific_files), force=True)
        
    else:
        print("🌍 Traduction de tous les fichiers .rst trouvés")
        files = []
        # Chercher seulement dans les répertoires source, pas dans locale
        for source_dir in ["documentation_main", "documentation_clients"]:
            source_path = ROOT_DIR / source_dir
            if source_path.exists():
                for file_path in source_path.rglob("*.rst"):
                    files.append(file_path)
        process_rst_files(files, force=False)


if __name__ == "__main__":
    main()