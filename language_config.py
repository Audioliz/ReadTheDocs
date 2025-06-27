# Configuration for language selection

# Default language is English
default_language = "en"

# Supported languages
languages = {
    "en": "English",
    "fr": "Français"
}

# Function to get the selected language
def get_language():
    import os
    lang = os.getenv("AUDIOLIZ_LANG", default_language)
    if lang not in languages:
        lang = default_language
    return lang
