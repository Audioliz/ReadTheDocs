#!/bin/bash

# Script de gestion des traductions pour Audioliz Documentation
# Usage: ./scripts/translate.sh [command]

set -e

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Fonction d'aide
show_help() {
    echo -e "${BLUE}Script de gestion des traductions Audioliz${NC}"
    echo ""
    echo "Usage: $0 [command]"
    echo ""
    echo "Commandes disponibles:"
    echo "  generate    - Génère les fichiers de template (.pot)"
    echo "  update      - Met à jour les fichiers de traduction (.po)"
    echo "  build       - Compile les fichiers de traduction (.mo)"
    echo "  clean       - Nettoie les fichiers temporaires"
    echo "  status      - Affiche le statut des traductions"
    echo "  help        - Affiche cette aide"
    echo ""
    echo "Exemples:"
    echo "  $0 generate"
    echo "  $0 update"
    echo "  $0 build"
}

# Fonction pour générer les templates
generate_templates() {
    echo -e "${BLUE}Génération des fichiers de template...${NC}"
    
    # Vérifier que l'environnement virtuel est activé
    if [[ -z "$VIRTUAL_ENV" ]]; then
        echo -e "${YELLOW}Attention: Environnement virtuel non détecté${NC}"
        echo "Activez votre environnement virtuel: source .env/bin/activate"
        exit 1
    fi
    
    make gettext
    echo -e "${GREEN}✓ Templates générés dans _build/gettext/${NC}"
}

# Fonction pour mettre à jour les traductions
update_translations() {
    echo -e "${BLUE}Mise à jour des fichiers de traduction...${NC}"
    
    # Vérifier que l'environnement virtuel est activé
    if [[ -z "$VIRTUAL_ENV" ]]; then
        echo -e "${YELLOW}Attention: Environnement virtuel non détecté${NC}"
        echo "Activez votre environnement virtuel: source .env/bin/activate"
        exit 1
    fi
    
    # Mettre à jour l'anglais
    sphinx-intl update -p _build/gettext -l en
    echo -e "${GREEN}✓ Fichiers .po mis à jour pour l'anglais${NC}"
}

# Fonction pour compiler les traductions
build_translations() {
    echo -e "${BLUE}Compilation des fichiers de traduction...${NC}"
    
    # Vérifier que l'environnement virtuel est activé
    if [[ -z "$VIRTUAL_ENV" ]]; then
        echo -e "${YELLOW}Attention: Environnement virtuel non détecté${NC}"
        echo "Activez votre environnement virtuel: source .env/bin/activate"
        exit 1
    fi
    
    sphinx-intl build
    echo -e "${GREEN}✓ Fichiers .mo compilés${NC}"
}

# Fonction pour nettoyer
clean() {
    echo -e "${BLUE}Nettoyage des fichiers temporaires...${NC}"
    
    # Supprimer les fichiers .mo
    find locale -name "*.mo" -delete
    echo -e "${GREEN}✓ Fichiers .mo supprimés${NC}"
    
    # Supprimer le dossier _build
    if [[ -d "_build" ]]; then
        rm -rf _build
        echo -e "${GREEN}✓ Dossier _build supprimé${NC}"
    fi
}

# Fonction pour afficher le statut
show_status() {
    echo -e "${BLUE}Statut des traductions:${NC}"
    echo ""
    
    # Compter les fichiers .po
    fr_count=$(find locale/fr/LC_MESSAGES -name "*.po" 2>/dev/null | wc -l)
    en_count=$(find locale/en/LC_MESSAGES -name "*.po" 2>/dev/null | wc -l)
    
    echo -e "🇫🇷 Français: ${fr_count} fichiers .po"
    echo -e "🇬🇧 English: ${en_count} fichiers .po"
    echo ""
    
    # Vérifier les traductions manquantes
    if [[ -d "locale/en/LC_MESSAGES" ]]; then
        echo -e "${BLUE}Traductions en anglais:${NC}"
        for po_file in locale/en/LC_MESSAGES/*.po; do
            if [[ -f "$po_file" ]]; then
                filename=$(basename "$po_file")
                translated=$(grep -c "^msgstr" "$po_file" || echo "0")
                untranslated=$(grep -c "^msgstr \"\"" "$po_file" || echo "0")
                total=$((translated + untranslated))
                if [[ $total -gt 0 ]]; then
                    percentage=$(( (translated * 100) / total ))
                    echo -e "  ${filename}: ${translated}/${total} (${percentage}%)"
                fi
            fi
        done
    fi
}

# Gestion des commandes
case "${1:-help}" in
    "generate")
        generate_templates
        ;;
    "update")
        update_translations
        ;;
    "build")
        build_translations
        ;;
    "clean")
        clean
        ;;
    "status")
        show_status
        ;;
    "help"|*)
        show_help
        ;;
esac 