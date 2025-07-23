Métadonnées des Appels
======================

Ajout ou Modification de Métadonnées
------------------------------------
Les métadonnées se réfèrent à des informations contextuelles supplémentaires attachées à un appel (telles que le nom de la campagne, l'ID CRM, ou le canal). 
Certaines métadonnées sont automatiquement stockées dans le champ `crm_metadata` dans la base de données, mais vous pouvez également définir et gérer des **champs de métadonnées personnalisés** pour des actions spécifiques.

Pour gérer les métadonnées pour une action spécifique :

- Allez à la page **Actions**

.. image:: /_static/choisir_page_action.png
  :width: 550
  :alt: Liste du tableau de bord

- Sélectionnez la fiche de score que vous souhaitez configurer en cliquant sur l'icône de l'œil  

.. image:: /_static/choisir_action.png
  :width: 550
  :alt: Liste du tableau de bord

- Ouvrez l'onglet **Métadonnées**

.. image:: /_static/choisir_meta.png
  :width: 550
  :alt: Liste du tableau de bord

Là, vous pouvez :

- ➕ **Ajouter une nouvelle métadonnée** en cliquant sur l'icône plus (`+`)  

.. image:: /_static/ajouter_meta.png
  :width: 400
  :alt: Liste du tableau de bord

- ✏️ **Modifier les métadonnées existantes** en cliquant directement sur la ligne de métadonnées

Pour chaque champ de métadonnées, vous pouvez définir :

.. image:: /_static/creation_meta.png
  :width: 550
  :alt: Liste du tableau de bord


- **Nom** : Le nom interne de la métadonnée, affiché dans l'onglet de configuration des métadonnées de la fiche de score.

- **Étiquette** : Le nom d'affichage montré dans la **Page d'Appel**.

- **Groupe** : La section de la **Page d'Appel** où cette métadonnée apparaîtra.

- **Valeur par défaut** : La valeur de repli utilisée si la métadonnée est manquante ou vide dans les données d'appel.  

**Astuce** : Si vous voulez que la question soit posée, c'est-à-dire *incluse dans l'invite envoyée à l'IA*, même lorsque la métadonnée est présente mais que sa valeur est vide (c'est-à-dire que le champ est défini pour l'appel mais n'a pas de valeur), alors définissez la **valeur par défaut à un espace simple (`` ``)**.

Cela garantit que l'espace réservé pour la métadonnée sera remplacé par une chaîne vide, et que la question ne sera pas omise lors de l'analyse.

Pourquoi les Métadonnées sont Importantes dans les Questions
------------------------------------------------------------
Certaines données nécessaires pour une question (comme un nom de campagne ou un type de produit) varient d'un appel à l'autre. Au lieu de créer plusieurs versions de la même question, vous pouvez **insérer dynamiquement des métadonnées** en utilisant le symbole `$` dans le texte de la question.

Exemple :
Quels arguments ont été donnés pour la campagne $NOM_DE_LA_CAMPAGNE