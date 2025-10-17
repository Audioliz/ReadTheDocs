# Configuration de l'automatisation du déploiement

Ce document explique comment configurer et utiliser le système d'automatisation du déploiement de la documentation.

## 🚀 Vue d'ensemble

Le système automatise les 4 étapes suivantes :
1. **Traduction** : Traduction automatique des fichiers .rst avec OpenAI
2. **Commit** : Commit automatique des traductions sur la branche main
3. **Merge** : Merge automatique vers toutes les branches clients
4. **Déploiement** : ReadTheDocs détecte les changements et reconstruit la documentation

## ⚙️ Configuration initiale

### 1. Configurer les secrets GitHub

Dans votre repository GitHub :
1. Allez dans **Settings > Secrets and variables > Actions**
2. Dans l'onglet **Repository secrets**
3. Cliquez sur **New repository secret**
4. Ajoutez :

```
Nom: OPENAI_API_KEY
Valeur: votre-cle-api-openai
```

**Note** : Utilisez Repository secrets (pas Environment ou Organization) pour ce projet.

### 2. Vérifier la structure des branches

Assurez-vous que les branches suivantes existent dans votre repository :
- `main` (branche principale)
- `bruneau`
- `wonderbox` 
- `fidelis`
- `audioliz`

## 🔄 Fonctionnement automatique

### Déclenchement automatique

Le workflow se déclenche automatiquement dans ces cas :
- **Push sur main** : Quand du code est poussé directement sur main
- **Merge de PR** : Quand une Pull Request est mergée sur main
- **Modifications de documentation** : Seulement si des fichiers dans `documentation_main/` ou `documentation_clients/` sont modifiés

### Étapes du workflow

1. **Détection des changements** : Le workflow vérifie s'il y a des modifications de documentation
2. **Traduction** : Utilise OpenAI pour traduire les fichiers .rst modifiés
3. **Commit intelligent** : Ne committe que s'il y a des changements de traduction
4. **Merge automatique** : Synchronise toutes les branches clients avec main
5. **Notification** : ReadTheDocs détecte les changements et reconstruit

## 🛠️ Utilisation manuelle

### Script de déploiement unifié

Pour déclencher manuellement le processus complet :

```bash
# Définir la clé API OpenAI
export OPENAI_API_KEY="votre-cle-api"

# Exécuter le déploiement
./scripts/deploy.sh
```

### Traduction seule

Pour traduire seulement (sans commit/merge) :

```bash
export OPENAI_API_KEY="votre-cle-api"
python scripts/translate.py
```

### Merge des branches seulement

Pour synchroniser les branches clients :

```bash
./scripts/git_merge_client_branches.sh
```

## 📁 Structure des fichiers

```
.github/workflows/
├── deploy-documentation.yml    # Workflow GitHub Actions principal

scripts/
├── deploy.sh                   # Script de déploiement unifié
├── translate.py               # Script de traduction (modifié)
├── git_merge_client_branches.sh # Script de merge (existant)

documentation_main/            # Documentation principale
documentation_clients/         # Documentation spécifique clients
locale/                       # Traductions générées automatiquement
```

## 🔧 Personnalisation

### Ajouter un nouveau client

1. **Créer la branche** : Créer une nouvelle branche basée sur main
2. **Modifier le script de merge** : Ajouter le client dans `scripts/git_merge_client_branches.sh`
3. **Configuration ReadTheDocs** : Ajouter le projet dans ReadTheDocs

### Modifier les paramètres de traduction

Dans `scripts/translate.py`, vous pouvez ajuster :
- `LANGUAGES` : Langues à traduire
- `MAX_NB_FILES_TRANSLATED` : Nombre maximum de fichiers traduits par exécution
- `MODEL` : Modèle OpenAI utilisé

## 🐛 Dépannage

### Le workflow ne se déclenche pas

- Vérifiez que les fichiers modifiés sont dans `documentation_main/` ou `documentation_clients/`
- Vérifiez que le push est bien sur la branche `main`

### Erreur de traduction

- Vérifiez que `OPENAI_API_KEY` est correctement configuré
- Vérifiez que vous avez des crédits OpenAI disponibles
- Consultez les logs GitHub Actions pour plus de détails

### Conflits de merge

- Le script gère automatiquement les merges simples
- En cas de conflits complexes, une intervention manuelle peut être nécessaire
- Consultez les logs pour identifier les branches problématiques

## 📊 Monitoring

### Logs GitHub Actions

Consultez l'onglet **Actions** de votre repository GitHub pour :
- Voir l'historique des déploiements
- Consulter les logs détaillés
- Identifier les erreurs

### Vérification ReadTheDocs

Après un déploiement réussi :
1. Allez sur votre projet ReadTheDocs
2. Vérifiez que les builds sont déclenchés
3. Consultez les logs de build pour identifier d'éventuels problèmes

## 🔒 Sécurité

- La clé API OpenAI est stockée comme secret GitHub
- Les commits automatiques sont marqués avec `[skip ci]` pour éviter les boucles
- Le workflow respecte les permissions du repository

## 📞 Support

En cas de problème :
1. Consultez les logs GitHub Actions
2. Vérifiez la configuration des secrets
3. Testez manuellement avec `./scripts/deploy.sh`
4. Contactez l'équipe de développement si nécessaire
