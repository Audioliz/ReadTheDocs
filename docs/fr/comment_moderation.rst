Gérer les Commentaires et les Retours
=====================================

1. Comment ajouter un commentaire à un enregistrement analysé ?
---------------------------------------------------------------

Vous pouvez ajouter un commentaire soit au niveau des réponses à chaque question, soit dans le champ de commentaire situé juste après la transcription. Voici les étapes à suivre :

- Choisissez un statut pour le commentaire dans le champ DEBUG-STATUS, le statut doit être :
       OUVERT lorsque vous posez une question ou laissez un commentaire
       RÉPONDU lorsque quelqu'un répond à votre commentaire
       FERMÉ lorsque vous avez la réponse correcte à votre commentaire
- Choisissez le niveau d'importance de votre commentaire :
       Normal
       Moyen
       Élevé

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/commentaire_enregistrement.png" width="600" alt="Ajouter un commentaire à un enregistrement analysé">
   </div>

2. Comment trouver et répondre aux commentaires laissés sur un appel analysé ?
-------------------------------------------------------------------------------

Vous devez cliquer sur le champ "commentaire", un onglet s'ouvrira où vous pourrez filtrer par date d'appel, agent, ID CRM.
Pour trouver les commentaires laissés, cliquez sur le champ "DEBUG STATUS" et sélectionnez l'option "OUVERT" pour afficher tous les appels analysés où un commentaire a été laissé. À ce stade, vous avez la possibilité de visualiser rapidement tous les commentaires laissés sur les appels en cliquant sur les deux flèches à côté de "👁️‍🗨️". Ou répondez aux commentaires en cliquant sur "👁️‍🗨️", en ouvrant la grille d'analyse des appels, et en suivant ces étapes :

- Changez le champ "DEBUG STATUS" en "Répondu"
- Sélectionnez la personne responsable de la réponse dans le champ "EN CHARGE".
- Répondez aux commentaires et questions dans le champ "RÉPONSE".

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/trouver_repondre_commentaires.png" width="600" alt="Trouver et répondre aux commentaires laissés sur un appel analysé">
   </div>

3. Supervision et Processus d'Ajout de Questions
------------------------------------------------

3.1. Amélioration Continue de la Formulation des Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dans le cadre de notre processus d'amélioration continue, nous visons à affiner la manière dont les questions sont rédigées. Cet effort implique à la fois notre équipe interne et le client, car des malentendus sur les besoins réels du client peuvent également entraîner des écarts.

Pour y remédier, nous avons mis en place une procédure parallèle du côté du client :

- Un superviseur examine et corrige manuellement les réponses incorrectes pour des questions spécifiques.

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/ameliore_continue.png" width="600" alt="Amélioration Continue de la Formulation des Questions">
   </div>

3.2 Processus d'Évaluation et de Supervision
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour garantir la qualité et l'exactitude des analyses basées sur l'IA, les superviseurs du côté client sont censés examiner et valider les réponses de l'IA pour des appels spécifiques. Les étapes suivantes décrivent la procédure d'évaluation recommandée :

- Accédez à la page d'appel qui doit être examinée.

- Remplissez le champ **Contre-évaluation par** avec le nom du superviseur.

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/champs_a _remplir.png" width="600" alt="Dashboard list">
   </div>

Pour aider notre équipe à mieux comprendre les corrections, il est fortement encouragé d'ajouter un commentaire au format suivant :

- question_name: réponse incorrecte de l'IA → réponse correcte | raison du changement

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/image_2025-06-18_141937013.png" width="600" alt="Dashboard list">
   </div>

En outre, le superviseur doit examiner les réponses générées par l'IA, cliquer sur les réponses incorrectes et les corriger manuellement. Il peut également laisser un commentaire plus détaillé sur chaque question si nécessaire.

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/changer_question.png" width="600" alt="Dashboard list">
   </div>

4. Comprendre le tableau de bord de comparaison IA vs Humain
------------------------------------------------------------

Cette page vous permet d'explorer les différences entre les évaluations faites par l'IA et celles faites par les réviseurs humains.

1. Tableau des Scores
~~~~~~~~~~~~~~~~~~~~~

Ce tableau affiche, pour chaque contre-évaluateur et chaque appel, le score humain, le score IA, et la différence entre les deux.
Si un contre-évaluateur (par exemple Hayat) n'apparaît pas, cela signifie qu'aucun score humain n'a été enregistré pour la période ou les filtres sélectionnés.

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/Score_Table.png" width="800" alt="Tableau des scores par contre-évaluateur">
   </div>

2. Évolution de l'écart moyen entre les scores IA et humains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce graphique montre la tendance de la différence moyenne entre les scores humains et IA au fil du temps (jour, semaine ou mois selon les filtres).

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/Evolution of the average gap between IA and human scores.png" width="800" alt="Graphique montrant l'écart moyen au fil du temps">
   </div>

3. Tableau de Précision par Question
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce visuel présente, pour chaque question, le pourcentage de réponses correctes et incorrectes par l'IA (basé sur la validation humaine) par contre-évaluateur.

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/Question-wise Accuracy Table.png" width="800" alt="Précision par question et réviseur">
   </div>

4. Détails Appel par Appel
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce tableau détaillé montre l'ID de l'appel, le nom de l'agent, le contre-évaluateur, la question évaluée, la réponse humaine, la réponse IA, et si la réponse de l'IA était correcte ou non.

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/Call-by-Call Details.png" width="800" alt="Précision par question et réviseur">
   </div>
