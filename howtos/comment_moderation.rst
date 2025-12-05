Commentaires et Retours
=====================

1.Comment ajouter un commentaire à un enregistrement analysé ?
---------------------------------------------------

Les commentaires sont importants pour votre équipe technique Audioliz, afin de voir ce qu'ils peuvent améliorer sur la fiche d'évaluation.

Vous pouvez ajouter un commentaire sur chaque question, ou dans le champ de commentaire situé après la transcription. Une fois que vous avez ajouté un commentaire, vous devez suivre les étapes suivantes : 

- Choisissez un statut pour le commentaire dans le champ DEBUG-STATUS, le statut doit être :
       OPEN lorsque vous laissez un commentaire<br>
       REPLIED lorsque l'équipe technique répond à votre commentaire<br>
       CLOSED lorsque vous avez validé la réponse de votre équipe de support Audioliz <br>
- Vous pouvez également choisir le niveau d'importance de votre commentaire : 
       Normal<br>
       Moyen <br>
       Élevé<br>



2. Comment trouver et répondre aux commentaires laissés sur un appel analysé ?
---------------------------------------------------------------------

Vous devez cliquer sur le champ "commentaire", un onglet s'ouvrira où vous pourrez filtrer par date d'appel, agent, ID CRM. 
Pour trouver les commentaires laissés, cliquez sur le champ "DEBUG STATUS" et sélectionnez l'option "OPEN" pour afficher tous les appels analysés où un commentaire a été laissé. À ce stade, vous avez la possibilité de visualiser rapidement tous les commentaires laissés sur les appels en cliquant sur les deux flèches à côté de "👁️‍🗨️". Ou répondez aux commentaires en cliquant sur "👁️‍🗨️", ouvrant la grille d'analyse d'appel, et en suivant ces étapes :

- Changez le champ "DEBUG STATUS" en "Répondu" 
- Sélectionnez la personne responsable de la réponse dans le champ "EN CHARGE".
- Répondez aux commentaires et questions dans le champ "RÉPONSE".



3. Supervision et Processus d'Ajustement des Questions
---------------------------------------------------------

3.1. Amélioration Continue de la Formulation des Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dans le cadre de notre processus d'amélioration continue, nous visons à affiner la manière dont les questions sont rédigées. Cet effort implique à la fois notre équipe interne et le client, car les malentendus sur les besoins réels du client peuvent également conduire à des divergences.

Pour y remédier, nous avons mis en place une procédure parallèle du côté du client :

- Un superviseur examine et corrige manuellement les réponses incorrectes pour des questions spécifiques.

- Le superviseur doit remplir le champ **Évaluation par** avec son nom.

- Ils sont également encouragés à ajouter des commentaires expliquant les corrections effectuées.

De notre côté, nous nous engageons à ajuster les questions pertinentes en fonction des commentaires des superviseurs, dans le but de minimiser l'écart entre l'analyse de l'IA et l'évaluation humaine — un objectif que nous surveillons activement à travers la page IA / HUMAIN de notre tableau de bord BI.

.. image:: /_static/ecart_ia_hum.png
  :width: 600
  :alt: Liste du tableau de bord


3.2 Processus d'Évaluation et de Supervision
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pour garantir la qualité et la précision des analyses basées sur l'IA, les superviseurs du côté du client sont censés examiner et valider les réponses de l'IA pour des appels spécifiques. Les étapes suivantes décrivent la procédure d'évaluation recommandée :

- Accédez à la page d'appel qui doit être examinée.

- Remplissez le champ **Évaluation par** avec le nom du superviseur.

.. image:: /_static/champs_a_remplir.png
  :width: 600
  :alt: Liste du tableau de bord



Pour aider notre équipe à mieux comprendre les corrections, il est fortement encouragé d'ajouter un commentaire dans le format suivant :

- nom_de_la_question : réponse incorrecte de l'IA → réponse correcte | raison du changement

.. image:: /_static/image_2025-06-18_141937013.png
  :width: 600
  :alt: Liste du tableau de bord

De plus, le superviseur devrait examiner les réponses générées par l'IA, cliquer sur les réponses incorrectes et les corriger manuellement. Ils peuvent également laisser un commentaire plus détaillé sur chaque question si nécessaire.

.. image:: /_static/changer_question.png
  :width: 600
  :alt: Liste du tableau de bord


4. Comprendre le tableau de bord de comparaison IA vs Humain
---------------------------------------------------------

Cette page vous permet d'explorer les différences entre les évaluations faites par l'IA et celles faites par les évaluateurs humains.

1. Tableau des Scores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Ce tableau affiche, pour chaque contre-évaluateur et chaque appel, le score humain, le score de l'IA, et la différence entre les deux.
Si un contre-évaluateur (par exemple, Hayat) n'apparaît pas, cela signifie qu'aucun score humain n'a été enregistré pour la période ou les filtres sélectionnés.


.. image:: /_static/Score_Table.png
  :width: 800
  :alt: Tableau des scores par contre-évaluateur

2. Évolution de l'écart moyen entre les scores de l'IA et de l'humain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce graphique montre la tendance de la différence moyenne entre les scores humains et ceux de l'IA au fil du temps (jour, semaine, ou mois selon les filtres).

.. image:: /_static/Evolution_of_the_average_gap_between_IA_and_human_scores.png
  :width: 800
  :alt: Graphique en ligne montrant l'écart moyen au fil du temps

3. Tableau de Précision par Question
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette visualisation présente, pour chaque question, le pourcentage de réponses correctes et incorrectes de l'IA (basé sur la validation humaine) par contre-évaluateur.

.. image:: /_static/Question-wise_Accuracy_Table.png
  :width: 800
  :alt: Précision par question et évaluateur

4. Détails Appel par Appel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce tableau détaillé montre l'ID de l'appel, le nom de l'agent, le contre-évaluateur, la question évaluée, la réponse humaine, la réponse de l'IA, et si la réponse de l'IA était correcte ou non.

.. image:: /_static/Call-by-Call_Details.png
  :width: 800
  :alt: Précision par question et évaluateur