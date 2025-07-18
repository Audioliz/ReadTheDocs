Spécificités Bruneau
===================

.. note::
   Cette section contient les spécificités et personnalisations dédiées à l'implémentation Bruneau d'Audioliz.

Configuration spécifique
------------------------

Configuration particulière pour l'environnement Bruneau :

.. code-block:: python

   # Configuration spécifique Bruneau
   AUDIOLIZ_CONFIG = {
       'client_name': 'bruneau',
       'custom_branding': True,
       'max_file_size': '25MB',  # Limite augmentée
       'bruneau_features': True
   }

Personnalisations d'interface
----------------------------

Interface adaptée aux besoins spécifiques de Bruneau :

- Couleurs et logo personnalisés
- Workflows adaptés aux processus internes
- Intégrations spécifiques

Workflows particuliers
----------------------

Processus de travail spécifiques à Bruneau :

1. **Validation en deux étapes** : Toutes les modifications passent par une validation supplémentaire
2. **Export automatique** : Génération automatique de rapports au format requis
3. **Intégration CRM** : Synchronisation avec le système CRM de Bruneau

.. seealso::
   Pour plus de détails sur la configuration standard, consultez :doc:`configuration_in_audioliz` 