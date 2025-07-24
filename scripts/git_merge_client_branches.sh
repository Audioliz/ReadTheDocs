#!/bin/bash

# Script pour automatiser les opérations git merge sur plusieurs branches

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Liste des branches à traiter
BRANCHES=("bruneau" "wonderbox" "fidelis" "audioliz")

echo -e "${BLUE}=== Script de merge automatique ===${NC}"
echo -e "Branches à traiter: ${BRANCHES[*]}"
echo

# Vérifier que nous sommes dans un dépôt git
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}❌ Erreur: Ce répertoire n'est pas un dépôt git.${NC}"
    exit 1
fi

# Récupérer la branche courante
CURRENT_BRANCH=$(git branch --show-current)
echo -e "📍 Branche courante: ${CURRENT_BRANCH}"
echo

# Vérifier que la branche main existe
if ! git show-ref --verify --quiet refs/heads/main; then
    echo -e "${RED}❌ Erreur: La branche 'main' n'existe pas.${NC}"
    exit 1
fi

# Traiter chaque branche
for branch in "${BRANCHES[@]}"; do
    echo -e "${BLUE}🔄 Traitement de la branche: ${branch}${NC}"
    echo "----------------------------------------"
    
    # Vérifier si la branche existe
    if ! git show-ref --verify --quiet "refs/remotes/origin/${branch}"; then
        echo -e "${YELLOW}⚠️  La branche '${branch}' n'existe pas, passage à la suivante.${NC}"
        echo
        continue
    fi
    
    # Checkout de la branche
    echo -e "📋 Checkout de la branche '${branch}'..."
    if git checkout "${branch}"; then
        echo -e "${GREEN}✅ Checkout réussi de '${branch}'${NC}"
    else
        echo -e "${RED}❌ Échec du checkout de '${branch}'${NC}"
        echo
        continue
    fi
    
    # Merge avec main
    echo -e "🔄 Merge de 'main' dans '${branch}'..."
    if git merge main; then
        echo -e "${GREEN}✅ Merge réussi de 'main' dans '${branch}'${NC}"
        
        # Push de la branche après merge réussi
        echo -e "📤 Push de la branche '${branch}'..."
        if git push origin "${branch}"; then
            echo -e "${GREEN}✅ Push réussi de '${branch}'${NC}"
        else
            echo -e "${RED}❌ Échec du push de '${branch}'${NC}"
        fi
    else
        echo -e "${RED}❌ Échec du merge de 'main' dans '${branch}'${NC}"
        echo -e "${YELLOW}💡 Vous devrez résoudre les conflits manuellement.${NC}"
    fi
    
    echo
done

# Retourner à la branche main
echo -e "🔄 Retour à la branche main"
git checkout main

echo
echo -e "${BLUE}=== Fin du script ===${NC}" 