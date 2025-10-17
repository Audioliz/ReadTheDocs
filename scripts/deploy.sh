#!/bin/bash

# Script de déploiement unifié pour la documentation
# Automatise les 4 étapes du processus de déploiement

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Script de déploiement automatique ===${NC}"
echo

# Vérifier que nous sommes dans un dépôt git
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}❌ Erreur: Ce répertoire n'est pas un dépôt git.${NC}"
    exit 1
fi

# Vérifier que nous sommes sur la branche main
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo -e "${YELLOW}⚠️  Vous n'êtes pas sur la branche main (branche actuelle: $CURRENT_BRANCH)${NC}"
    read -p "Voulez-vous continuer quand même? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${RED}❌ Déploiement annulé${NC}"
        exit 1
    fi
fi

# Vérifier que la clé API OpenAI est définie
if [ -z "$OPENAI_API_KEY" ]; then
    echo -e "${RED}❌ Erreur: La variable d'environnement OPENAI_API_KEY n'est pas définie${NC}"
    echo "Veuillez définir votre clé API OpenAI:"
    echo "export OPENAI_API_KEY='votre-cle-api'"
    exit 1
fi

echo -e "${BLUE}📋 Étape 1/4: Traduction de la documentation${NC}"
echo "----------------------------------------"
if uv run python scripts/translate.py; then
    echo -e "${GREEN}✅ Traduction terminée${NC}"
else
    echo -e "${RED}❌ Erreur lors de la traduction${NC}"
    exit 1
fi
echo

# Vérifier s'il y a des changements de traduction
if git diff --quiet HEAD -- locale/; then
    echo -e "${YELLOW}📝 Aucun changement de traduction détecté${NC}"
    echo -e "${BLUE}📋 Étape 2/4: Pas de commit nécessaire${NC}"
    echo -e "${BLUE}📋 Étape 3/4: Pas de merge nécessaire${NC}"
else
    echo -e "${BLUE}📋 Étape 2/4: Commit des traductions sur main${NC}"
    echo "----------------------------------------"
    
    # Ajouter les fichiers de traduction
    git add locale/
    
    # Commit avec un message descriptif
    git commit -m "Auto-translate: Update translations

- Traduction automatique des fichiers .rst
- Généré par le script de déploiement automatique
- Date: $(date)"
    
    if git push origin main; then
        echo -e "${GREEN}✅ Commit et push réussis${NC}"
    else
        echo -e "${RED}❌ Erreur lors du push${NC}"
        exit 1
    fi
    echo

    echo -e "${BLUE}📋 Étape 3/4: Merge vers les branches clients${NC}"
    echo "----------------------------------------"
    if ./scripts/git_merge_client_branches.sh; then
        echo -e "${GREEN}✅ Merge vers les branches clients réussi${NC}"
    else
        echo -e "${RED}❌ Erreur lors du merge vers les branches clients${NC}"
        exit 1
    fi
    echo
fi

echo -e "${BLUE}📋 Étape 4/4: Déploiement terminé${NC}"
echo "----------------------------------------"
echo -e "${GREEN}✅ Déploiement automatique terminé avec succès!${NC}"
echo
echo -e "${BLUE}📚 Prochaines étapes:${NC}"
echo "• ReadTheDocs détectera automatiquement les changements"
echo "• La documentation sera reconstruite pour toutes les versions"
echo "• Les modifications seront disponibles sur tous les sites clients"
echo

# Afficher un résumé des branches mises à jour
echo -e "${BLUE}📋 Résumé des branches mises à jour:${NC}"
echo "• main: Documentation principale et traductions"
for branch in "bruneau" "wonderbox" "fidelis" "audioliz"; do
    if git show-ref --verify --quiet "refs/remotes/origin/${branch}"; then
        echo "• ${branch}: Branche client synchronisée"
    fi
done

echo
echo -e "${GREEN}🎉 Processus de déploiement terminé!${NC}"
