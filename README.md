Documentation Audioliz
######################

Etapes pour modifier le contenu de la documenation

a. Modifier la doc en anglais dans ```documentation_main```.rst.
e. Tu recommences dans les docs clients après les avoir mises à jour
    a. Git checkout bruneau
    b. Git merge main
        i. Il faut parfois résoure des conflits…
Nouveau flux pour la traduction
	export OPENAI_API_KEY=sk-
	./scripts/translate.py
Pour tester
	source .venv/bin/activate
	uv pip install -r requirements.txt           <<<<<<<< éventuellement
	export READTHEDOCS_VERSION=bruneau
	export READTHEDOCS_LANGUAGE=fr     <<<<<<<< éventuellement
	./scripts/local_build.sh
	cd _build/html ; python -m http.server 1700
http://localhost:1700/
