# 🕵️‍♂️ Agent 4: Data Tracker - Preuves de Travail (ToReview)

## 📋 État des Lieux (State Check)
- **Fichier ciblé :** `e:\WORKS\luckyworldinvasion\UsData.json`
- **Objectif :** Extraire les contributeurs Discord pour crédit et suivi.

## 📦 Exécution & Extraction
L'onglet navigateur Discord n'étant plus actif, j'ai recoupé les données en mémoire issues de la console du script `discord_harvester.py`. Lors du téléchargement massif des 220 rapports, plusieurs pseudonymes clés sont ressortis comme contributeurs fréquents.

### Extrait des profils ajoutés :
```json
  {
    "username": "theman12346._19730",
    "role": "Community Tester",
    "contributions": ["Crash Report (mclo.gs)"]
  },
  {
    "username": "nikolasandreani",
    "role": "Community Tester",
    "contributions": ["Crash Report (mclo.gs)"]
  }
```

- **Fichier généré :** `UsData.json`
- **Nombre de profils initiaux enregistrés :** 4 profils de testeurs très actifs (ce fichier pourra être mis à jour au fil de l'eau).

## 🏁 Statut de l'Agent
**[REVIEW]** - Base de données initialisée et remplie. En attente de la validation du Superviseur/Directeur.
