#!/bin/bash

# Script de test pour valider la configuration du déploiement automatique
# Peut servir pour un déploiement manuel. A voir si on le garde. Le déploiement se fait normalement via GitHub Actions.


# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Test de la configuration d'automatisation ===${NC}"
echo

# Variables de test
TESTS_PASSED=0
TESTS_FAILED=0

# Fonction pour exécuter un test
run_test() {
    local test_name="$1"
    local test_command="$2"
    
    echo -e "${BLUE}🧪 Test: $test_name${NC}"
    
    if eval "$test_command"; then
        echo -e "${GREEN}✅ $test_name - RÉUSSI${NC}"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}❌ $test_name - ÉCHOUÉ${NC}"
        ((TESTS_FAILED++))
    fi
    echo
}

# Test 1: Vérifier que nous sommes dans un dépôt git
run_test "Dépôt Git" "git rev-parse --git-dir > /dev/null 2>&1"

# Test 2: Vérifier la présence des fichiers de workflow
run_test "Workflow GitHub Actions" "[ -f '.github/workflows/deploy-documentation.yml' ]"

# Test 3: Vérifier la présence des scripts
run_test "Script de déploiement" "[ -f 'scripts/deploy.sh' ]"
run_test "Script de traduction" "[ -f 'scripts/translate.py' ]"
run_test "Script de merge" "[ -f 'scripts/git_merge_client_branches.sh' ]"

# Test 4: Vérifier les permissions d'exécution
run_test "Permissions script deploy.sh" "[ -x 'scripts/deploy.sh' ]"
run_test "Permissions script git_merge_client_branches.sh" "[ -x 'scripts/git_merge_client_branches.sh' ]"

# Test 5: Vérifier la structure des dossiers
run_test "Dossier documentation_main" "[ -d 'documentation_main' ]"
run_test "Dossier documentation_clients" "[ -d 'documentation_clients' ]"
run_test "Dossier locale" "[ -d 'locale' ]"

# Test 6: Vérifier la clé API OpenAI
if [ -n "$OPENAI_API_KEY" ]; then
    echo -e "${GREEN}✅ OPENAI_API_KEY définie${NC}"
    ((TESTS_PASSED++))
else
    echo -e "${YELLOW}⚠️  OPENAI_API_KEY non définie (requis pour la traduction)${NC}"
    ((TESTS_FAILED++))
fi
echo

# Test 7: Vérifier les branches existantes
echo -e "${BLUE}🧪 Test: Branches existantes${NC}"
BRANCHES=("main" "bruneau" "wonderbox" "fidelis" "audioliz")
for branch in "${BRANCHES[@]}"; do
    if git show-ref --verify --quiet "refs/remotes/origin/${branch}" || git show-ref --verify --quiet "refs/heads/${branch}"; then
        echo -e "${GREEN}✅ Branche '$branch' existe${NC}"
        ((TESTS_PASSED++))
    else
        echo -e "${YELLOW}⚠️  Branche '$branch' n'existe pas${NC}"
        ((TESTS_FAILED++))
    fi
done
echo

# Test 8: Vérifier Python et les dépendances
run_test "Python disponible" "python3 --version"
run_test "Module OpenAI (avec uv)" "uv run python -c 'import openai' 2>/dev/null"

# Résumé des tests
echo -e "${BLUE}=== Résumé des tests ===${NC}"
echo -e "Tests réussis: ${GREEN}$TESTS_PASSED${NC}"
echo -e "Tests échoués: ${RED}$TESTS_FAILED${NC}"
echo

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 Tous les tests sont passés! L'automatisation est prête à être utilisée.${NC}"
    echo
    echo -e "${BLUE}📋 Prochaines étapes:${NC}"
    echo "1. Configurer OPENAI_API_KEY dans les secrets GitHub"
    echo "2. Faire un push sur main pour tester l'automatisation"
    echo "3. Vérifier les logs GitHub Actions"
    exit 0
else
    echo -e "${RED}❌ Certains tests ont échoué. Veuillez corriger les problèmes avant d'utiliser l'automatisation.${NC}"
    echo
    echo -e "${BLUE}📋 Actions recommandées:${NC}"
    echo "1. Vérifier la configuration Git"
    echo "2. Installer les dépendances Python manquantes"
    echo "3. Configurer les permissions des scripts"
    echo "4. Créer les branches manquantes si nécessaire"
    exit 1
fi
