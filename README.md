# Documentation Audioliz

## Comment modifier le contenu de la documentation ?

### En ligne (modification simple)

#### 1. Créer une nouvelle branche
Si la modification concerne plusieurs fichiers, il est préférable de créer une nouvelle branche + PR. Car ReadtheDocs reconstruite des docs à chaque commit sur main.

* Branches -> new branch
  
  <img width="327" height="310" alt="image" src="https://github.com/user-attachments/assets/deb2e374-255c-4bc3-bf93-e8b789416c73" />

#### 2. Modifier la doc en anglais
```documentation_main``` : documentation qui concerne tous les clients
```documentation_clients``` : documentation spécifique aux clients

### En local

#### 1. Pour tester

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
