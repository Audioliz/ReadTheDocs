# Documentation Audioliz

## Comment modifier le contenu de la documentation ?

Il y a 2 façons de modifier la documentation : en ligne et en local. Pour des modifications ponctuelles, on peut le faire en ligne.
Les modifications sont automatiquement traduites et propagées aux versions clients.

### En ligne
Il suffit de modifier la documentation en anglais. 
 - ```documentation_main``` : documentation qui concerne tous les clients
 - ```documentation_clients``` : documentation spécifique aux clients

#### Utiliser une branche
Si la modification concerne plusieurs fichiers, il est préférable de créer une nouvelle branche + PR. Car ReadtheDocs reconstruit des docs à chaque commit sur main.

* Branches -> new branch
  
  <img width="150" height="150" alt="image" src="https://github.com/user-attachments/assets/deb2e374-255c-4bc3-bf93-e8b789416c73" />
* Créer un Pull Request.
* Squash merge
  
### En local

Cela nécessite d'installer le projet sur son ordinateur. Mais ça peut devenir nécessaire si on veut faire des modifications plus importantes : tables des matières, nouveaux clients, ajout d'images et de vidéo, ...

```
source .venv/bin/activate
uv pip install -r requirements.txt         #  <<<<<<<< éventuellement
export READTHEDOCS_VERSION=bruneau
export READTHEDOCS_LANGUAGE=fr    #  <<<<<<<< éventuellement, en fonction de la langue à tester
export OPENAI_API_KEY=xxxxx
./scripts/local_build.sh
cd _build/html ; python -m http.server 1700   # n'importe quel port libre
```
Et dans un navigateur : [http://localhost:1700/](url)

Au moment du commit, le déploiement se fait tout seul : traductions et merge vers les branches clients.

## Ajouter un nouveau client

### 1. Github
Cloner la branche main pour créer ```nouveau_client```

Les branches clients doivent toujours être identiques à ```main```. Elles sont juste nécessaires pour Readthedocs.

### 2. documentation/clients
 * Ajouter un dossier ```nouveau_client``` en s'inspirant des autres clients.
 * Ajouter le nouveau client dans ```scripts/clients.json``` 

### 3. ReadTheDocs
Ajouter une version de ce client dans chaque projet ReadTheDocs. Il y a un projet par langue.

## Rédaction du contenu

### 1. Structure
Toutes les pages doivent être dans des toctree. 
Sinon :
* Quand on ouvre la page directment on ne voit pas où elle se trouve (breadcrumb et menu de gauche)
* Les boutons "précédents" / "suivants" ne passent pas par cette page
		
### 2. Concision
Supprimer les mots qui n'apportent pas d'information. Exemple : préférer "Metadata" plutôt que "Manage Metadata in Audioliz".

### 3. Autres

* **|$|** : Le contenu entouré par ces balises n'est pas traduit

## Dev

### stack
* **GitHub** : Une branche par client. Elle contiennent toutes la même chose. Mais ReadTheDocs a besoin d'une branche par client. Il faut toujours préférer modifier la branche main. Car le worklow de déploiement merge depuis main vers les autres branches. 
* **reStructuredText** : markup langage utilisé pour rédiger le contenu
* **sphinx** : génére la doc à partir de reStructuredText
* **ReadTheDocs** : héberge la documentation. Un projet par langue. Dans chaque projet il y a une version par client, et la version principale : latest

### Déploiement automatique
* **GitHub Actions** : Execute le workflow ```deploy-documentation.yaml```. La traduction est faite automatiquement, par un LLM.
* **ReadTheDocs** : repère qu'il y a eu un changement sur une branche. Les versions (une par langue = une par projet RTD) construisent leur version statique en executant
* **pre_build.sh** : copie le contenu utile dans le répertoire racine. C'est lui qui sera utilisé par RTD pour construire la doc
* **Post_build.sh** : nettoie les fichiers et dossiers créés par pre_build.sh. Sert uniquement pour l'env de travail local.


