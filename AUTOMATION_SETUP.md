# Configuration de l'automatisation du déploiement

Ce document explique comment configurer et utiliser le système d'automatisation du déploiement de la documentation.

## 🚀 Vue d'ensemble

Le système automatise les 4 étapes suivantes :
1. **Traduction** : Traduction automatique des fichiers .rst avec OpenAI
2. **Commit** : Commit automatique des traductions sur la branche main
3. **Merge intelligent** : Merge automatique vers seulement les branches clients affectées
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
4. **Détection intelligente** : Détermine quels clients sont affectés par les changements
5. **Merge sélectif** : Met à jour seulement les branches clients concernées  
6. **Notification** : ReadTheDocs détecte les changements et reconstruit

## 🧠 Logique intelligente de détection

### **Détection des clients affectés**

Le système détermine intelligemment quelles branches clients mettre à jour :

#### **Changements dans `documentation_main/`**
- ✅ **Affecte TOUS les clients** (documentation générale)
- ✅ Merge vers toutes les branches : `bruneau`, `wonderbox`, `fidelis`, `audioliz`

#### **Changements dans `documentation_clients/[client]/`**
- ✅ **Affecte SEULEMENT le client concerné**
- ✅ Exemple : Modification dans `documentation_clients/fidelis/` → Merge seulement vers `fidelis`

#### **Changements dans `locale/` (traductions)**
- ✅ **Affecte TOUS les clients** (traductions partagées)

### **Exemples concrets**

```bash
# Cas 1: Modification dans documentation_main/
git diff --name-only HEAD~1 HEAD
# → documentation_main/howtos/new_feature.rst
# → Merge vers TOUTES les branches clients

# Cas 2: Modification spécifique à un client
git diff --name-only HEAD~1 HEAD  
# → documentation_clients/fidelis/specific_guide.rst
# → Merge SEULEMENT vers fidelis

# Cas 3: Traduction automatique
git diff --name-only HEAD~1 HEAD
# → locale/fr/documentation_main/howtos/new_feature.rst
# → Merge vers TOUTES les branches clients
```

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

**Note** : Le script de merge séparé n'existe plus. Le merge intelligent est intégré dans `./scripts/deploy.sh` et le workflow GitHub Actions.

## 📁 Structure des fichiers

```
.github/workflows/
├── deploy-documentation.yml    # Workflow GitHub Actions principal

scripts/
├── deploy.sh                   # Script de déploiement unifié
├── translate.py               # Script de traduction (modifié)
├── clients.json               # Configuration centralisée des clients (JSON)

documentation_main/            # Documentation principale
documentation_clients/         # Documentation spécifique clients
locale/                       # Traductions générées automatiquement
```

## 🔧 Personnalisation

### Ajouter un nouveau client

1. **Créer la branche** : Créer une nouvelle branche basée sur main
2. **Ajouter dans la configuration** : Modifier `scripts/clients.json`
   ```json
   {
     "clients": {
       "bruneau": 3,
       "wonderbox": 7,
       "fidelis": 1,
       "audioliz": 52,
       "nouveau_client": 99  // ← Une seule ligne !
     }
   }
   ```
3. **Créer la documentation** : Ajouter le dossier `documentation_clients/nouveau_client/`
4. **Configuration ReadTheDocs** : Ajouter le projet dans ReadTheDocs

**C'est tout !** L'automatisation détectera automatiquement le nouveau client.

### Format de configuration JSON

Le fichier `scripts/clients.json` utilise le format JSON pour être compatible avec tous les scripts :

```json
{
  "clients": {
    "bruneau": 3,
    "wonderbox": 7,
    "fidelis": 1,
    "audioliz": 52
  },
  "metadata": {
    "description": "Configuration centralisée des clients",
    "version": "1.0",
    "special_cases": {
      "latest": 0
    }
  }
}
```

**Structure du JSON :**
- **`clients`** : Objet associant chaque nom de client à son ID numérique
- **`metadata.special_cases`** : Cas spéciaux comme "latest" (ID 0)
- **`metadata`** : Informations sur la configuration

**Avantages du JSON :**
- ✅ Compatible avec Bash (via `jq`)
- ✅ Compatible avec Python (via `json`)
- ✅ Compatible avec GitHub Actions
- ✅ Format standard et lisible
- ✅ Configuration centralisée complète

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
