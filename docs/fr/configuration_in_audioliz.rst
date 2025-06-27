Configuration dans Audioliz
===========================

1. Créer une question
---------------------

Vous pouvez modifier/créer autant de questions que vous le souhaitez dans votre feuille de suivi. Il existe trois types de questions :

1.1 Question Texte
~~~~~~~~~~~~~~~~~~

Vous pouvez choisir une question texte lorsque la réponse est un paragraphe. Par exemple : 'Donnez-moi le résumé de l'appel' ou 'Quels sujets ont été abordés dans l'appel ?'

Si vous avez une question oui/non, il est préférable de ne pas sélectionner ce type de question.

Créons une question texte :

.. raw:: html

   <div style="text-align: center;">
     <video width="640" height="360" controls>
       <source src="_static\create_question_text.mp4" type="video/mp4">
     </video>
   </div>

1.2 Question à un choix
~~~~~~~~~~~~~~~~~~~~~~~

Une question à choix unique est utilisée lorsqu'il n'y a qu'une seule réponse possible. Elle est généralement utilisée avec des questions oui/non.

Essayons :

.. raw:: html

   <div style="text-align: center;">
     <video width="640" height="360" controls>
       <source src="_static\create_question_ONE CHOICE.mp4" type="video/mp4">
     </video>
   </div>

1.3 Question à choix multiples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Une question à choix multiples est utilisée lorsque la réponse n'est pas nécessairement unique. Dans ce cas, vous pouvez avoir plusieurs réponses.

Voyons un exemple :

.. raw:: html

   <div style="text-align: center;">
     <video width="640" height="360" controls>
       <source src="..\_static\create_question_MULTIPLE CHOICES.mp4" type="video/mp4">
     </video>
   </div>

2. Modifier les paramètres de la feuille de suivi
-------------------------------------------------

Vous pouvez modifier de nombreux paramètres dans votre grille de suivi. Voyons comment :

.. raw:: html

   <div style="text-align: center;">
     <video width="640" height="360" controls>
       <source src="..\_static\action.mp4" type="video/mp4">
     </video>
   </div>

3. Gestion des métadonnées dans Audioliz
----------------------------------------

3.1 Ajouter ou modifier des métadonnées
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les métadonnées font référence à des informations contextuelles supplémentaires attachées à un appel (comme le nom de la campagne, l'ID CRM ou le canal). Certaines métadonnées sont automatiquement stockées dans le champ `crm_metadata` de la base de données, mais vous pouvez également définir et gérer des **champs de métadonnées personnalisés** pour des actions spécifiques.

Pour gérer les métadonnées pour une action spécifique :

- Accédez à la page **Actions**

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/choisir_page_action.png" width="550" alt="Liste des tableaux de bord">
   </div>

- Sélectionnez la grille que vous souhaitez configurer en cliquant sur l'icône en forme d'œil

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/choisir_action.png" width="550" alt="Liste des tableaux de bord">
   </div>

- Ouvrez l'onglet **Métadonnées**

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/choisir_meta.png" width="550" alt="Liste des tableaux de bord">
   </div>

Là, vous pouvez :

- **Ajouter une nouvelle métadonnée** en cliquant sur l'icône plus (`+`)

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/ajouter_meta.png" width="400" alt="Liste des tableaux de bord">
   </div>

- **Modifier les métadonnées existantes** en cliquant directement sur la ligne de métadonnées

Pour chaque champ de métadonnées, vous pouvez définir :

.. raw:: html

   <div style="text-align: center;">
     <img src="_static/creation_meta.png" width="550" alt="Liste des tableaux de bord">
   </div>

- **Nom** : Le nom interne de la métadonnée, affiché dans la page **Actions**.

- **Étiquette** : Le nom affiché dans la **Page d'appel**.

- **Groupe** : La section de la **Page d'appel** où cette métadonnée apparaîtra.

- **Valeur par défaut** : La valeur de repli utilisée si la métadonnée est manquante ou vide dans les données de l'appel.

**Astuce** : Si vous souhaitez que la question soit posée, c'est-à-dire *incluse dans le prompt envoyé à l'IA*, même lorsque la métadonnée est présente mais que sa valeur est vide (c'est-à-dire que le champ est défini pour l'appel mais n'a pas de valeur), alors définissez la **valeur par défaut sur un espace unique (` `)**.

Cela garantit que l'espace réservé à la métadonnée sera remplacé par une chaîne vide, et que la question ne sera pas ignorée lors de l'analyse.

3.2 Pourquoi les métadonnées sont importantes dans les questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Certaines données nécessaires à une question (comme le nom d'une campagne ou le type de produit) varient d'un appel à l'autre. Au lieu de créer plusieurs versions de la même question, vous pouvez **insérer des métadonnées dynamiquement** en utilisant le symbole `$` dans le texte de la question.

Exemple :
Quels arguments ont été donnés pour la campagne $CAMPAIGN_NAME

4. Gestion des rôles utilisateurs dans Audioliz
-----------------------------------------------

Dans Audioliz, chaque utilisateur a un rôle qui définit ce qu'il peut faire et accéder dans la plateforme. Les rôles sont utilisés pour contrôler les permissions en fonction des responsabilités, telles que la lecture des données, la modification des grilles, la gestion des utilisateurs ou les commentaires sur les appels.

4.1 Rôles prédéfinis dans Audioliz
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rôle	Description
Admin	: Accès complet à toutes les fonctionnalités
Superviseur :	Peut tout faire sauf l'administration des utilisateurs
Superviseur externe :	Comme les agents, mais peut également commenter les appels et modifier les métadonnées
Agent	: Peut consulter les appels et répondre aux grilles, mais ne peut pas gérer les utilisateurs ou les paramètres

Vous pouvez voir cette liste en naviguant vers Configuration > Utilisateurs > RÔLES :

.. raw:: html

   <div style="text-align: center;">
    <img src="_static/roles_list.png" width="720" alt="Liste des rôles disponibles">
   </div>

En cliquant sur n'importe quel rôle (par exemple admin), vous verrez les permissions détaillées attachées à ce rôle :

.. raw:: html

 <div style="text-align: center;"> 
  <img src="_static/permissions_admin.png" width="720" alt="Permissions du rôle admin">
 </div>

Les permissions contrôlent quels types de rôles peuvent accéder ou effectuer certaines opérations sur les appels

4.2 Comment modifier le rôle d'un utilisateur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les utilisateurs administrateurs peuvent attribuer ou modifier les rôles des utilisateurs :

Étapes :
Accédez à Configuration > Utilisateurs dans le menu de gauche.

Vous verrez les utilisateurs listés. Cliquez sur l'icône en forme d'œil pour voir les profils individuels :

.. raw:: html

  <div style="text-align: center;"> 
   <img src="_static/user_list.png" width="720" alt="Liste des utilisateurs"> 
  </div>

Dans la page de profil, faites défiler jusqu'à la section Rôles et cliquez dessus :

.. raw:: html

 <div style="text-align: center;">
   <img src="_static/edit_user.png" width="720" alt="Profil utilisateur avec sélection de rôle"> 
 </div>

Un menu déroulant apparaîtra. Vous pouvez sélectionner un ou plusieurs rôles dans la liste :

.. raw:: html

  <div style="text-align: center;"> 
   <img src="_static/choose_role.png" width="720" alt="Choisir le rôle utilisateur"> 
  </div>

Cliquez sur Enregistrer pour confirmer vos modifications.

💡 Astuce
Si vous ne voyez pas les options de rôle ou ne pouvez pas les modifier, cela signifie que votre compte n'a pas de privilèges administratifs. Vous devrez contacter un administrateur pour mettre à jour les rôles.
