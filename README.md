# Documentation Audioliz

## Comment modifier le contenu de la documentation ?

### En ligne
Les modifications en ligne ne sont pas traduites automatiquement, ni propagées aux versions clients. Ce sera fait lors des prochaines modifications par un développeur (modification en mode "local", cf ci-dessous).

#### 1. Créer une nouvelle branche
Si la modification concerne plusieurs fichiers, il est préférable de créer une nouvelle branche + PR. Car ReadtheDocs reconstruit des docs à chaque commit sur main.

* Branches -> new branch
  
  <img width="327" height="310" alt="image" src="https://github.com/user-attachments/assets/deb2e374-255c-4bc3-bf93-e8b789416c73" />

#### 2. Modifier la doc en anglais
```documentation_main``` : documentation qui concerne tous les clients
```documentation_clients``` : documentation spécifique aux clients

#### 3. Modifier les traductions (optionnel)

Dans ```locale```.

#### 4. Merge

* Créer un Pull Request.
* Squash merge
  
### En local

#### 1. Tester

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

#### 2. Déployer

* tester ?
* traduire : ``` ./scripts/translate.py```
* commit sur la branche main
* ./scripts/git_merge_client_branches.sh 

## Ajouter un nouveau client

### 1. Github
Cloner la branche main pour créer ```nouveau_client```

Les branches clients doivent toujours être identiques à ```main```. Elles sont juste nécessaires pour Readthedocs.

### 2. documentation/clients
 * Ajouter un dossier ```nouveau_client``` en s'inspirant des autres clients.
 * Ajouter le nouveau client dans ```scripts/git_merge_client_branches.sh``` 
 * Eventuellement ajouter une ligne dans ```clients_map```, dans ```pre_build.py```. C'est utile pour écrire des parties spécifiques à ce client directement dans la doc commune.

### 3. ReadTheDocs
Ajouter une version de ce client dans chaque projet ReadTheDocs. Il y a un projet par langue.

## Stack

* **reStructuredText** : markup langage utilisé pour rédiger le contenu
* **sphinx** : génére la doc à partir de reStructuredText
* **ReadTheDocs** : héberge la documentation

La traduction est faite automatiquement, par un LLM.

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
