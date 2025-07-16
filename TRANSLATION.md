# Guide de Traduction - Audioliz Documentation

Ce guide explique comment contribuer aux traductions de la documentation Audioliz.

## Architecture de Traduction

La documentation utilise un système de traduction multilingue avec :
- **Read the Docs** : Hébergement et génération des versions traduites
- **Weblate** : Plateforme de traduction collaborative
- **GitHub** : Synchronisation et versioning

## Langues Supportées

- 🇫🇷 **Français** (langue par défaut)
- 🇬🇧 **English** (anglais)

## Structure des Fichiers

```
locale/
├── fr/                    # Français (source)
│   └── LC_MESSAGES/
│       ├── index.po
│       ├── intro.po
│       └── ...
└── en/                    # English
    └── LC_MESSAGES/
        ├── index.po
        ├── intro.po
        └── ...
```

## Processus de Traduction

### 1. Ajout de Nouveau Contenu

Quand vous ajoutez du nouveau contenu en français :

1. Écrivez le contenu dans les fichiers `.rst`
2. Utilisez la fonction `_()` pour les chaînes traduisibles :
   ```rst
   .. _installation:
   
   Installation
   ============
   
   Bienvenue dans la documentation d'Audioliz.
   ```

### 2. Génération du Template

```bash
make gettext
```

Cette commande génère les fichiers `.pot` dans `_build/gettext/`.

### 3. Mise à Jour des Fichiers de Traduction

```bash
sphinx-intl update -p _build/gettext -l en
```

Cette commande met à jour les fichiers `.po` avec les nouvelles chaînes.

### 4. Traduction via Weblate

1. Connectez-vous à votre instance Weblate
2. Naviguez vers le projet "Audioliz Documentation"
3. Sélectionnez le composant "Documentation"
4. Traduisez les chaînes en anglais
5. Weblate commitera automatiquement les changements

### 5. Synchronisation GitHub

Le workflow GitHub Actions (`/.github/workflows/weblate-sync.yml`) :
- Se déclenche sur les changements dans `locale/`
- Met à jour les fichiers de traduction
- Commite les changements automatiquement

## Configuration Weblate

Le fichier `weblate.yml` contient la configuration pour :
- Définir les langues supportées
- Configurer les composants de traduction
- Définir les notifications GitHub

## Développement Local

### Construire la Documentation en Anglais

```bash
make -e SPHINXOPTS="-D language='en'" html
```

### Construire la Documentation en Français

```bash
make -e SPHINXOPTS="-D language='fr'" html
```

### Vérifier les Traductions

```bash
sphinx-intl build
```

## Bonnes Pratiques

1. **Cohérence** : Utilisez la même terminologie dans toutes les langues
2. **Contexte** : Fournissez du contexte pour les traducteurs
3. **Tests** : Vérifiez que la documentation se construit correctement
4. **Révision** : Faites réviser les traductions par des locuteurs natifs

## Support

Pour toute question sur les traductions :
- Ouvrez une issue sur GitHub
- Contactez l'équipe de traduction
- Consultez la documentation Weblate 