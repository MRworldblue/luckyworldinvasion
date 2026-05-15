# Rapport de Mission : Agent 11

## Statut : [REVIEW]

## Actions Réalisées

1. **Vérification de l'Index Packwiz (`pack/mods/`)** :
   - Recherche approfondie des mods `gunsmithlib`, `apotheosis_modern_ragnarok` et `geckoanimfix`.
   - Les fichiers `.pw.toml` (ou `.jar`) pour ces mods étaient **déjà absents** du dossier `mods/` (très probablement purgés par l'Agent 8).

2. **Purge des Dépendances Orphelines (Configs & Data)** :
   - Bien que les mods aient été retirés, des configurations et des scripts KubeJS orphelins chargeaient toujours des données liées à ces mods, causant les crashs serveur/client.
   - Suppression du fichier : `hardcore_project/pack/config/gunsmithlib-common.toml`
   - Suppression du fichier : `hardcore_project/pack/config/apotheosis_modern_ragnarok-common.toml`
   - Suppression du dossier entier : `hardcore_project/pack/kubejs/data/apotheosis_modern_ragnarok/`
   - Suppression du dossier entier : `hardcore_project/pack/kubejs/data/apotheotic_additions/affixes/ragnarok/`
   - Suppression de dossiers KubeJS obsolètes liés à TACZ (et ses addons) : `kubejs/data/tacz/` et `kubejs/data/applied_armorer/`

3. **Mise à Jour de l'Index Packwiz** :
   - Exécution de `packwiz refresh` dans `hardcore_project/pack/` pour nettoyer proprement l'`index.toml` de tous les restes de ces dépendances.

## Conclusion & Recommandations

Les crashs constatés par l'Agent 00 étaient dus au fait que l'instance cliente utilisée pour le test contenait toujours des fichiers de ces mods ou que le jeu tentait de charger les datapacks/configs associés qui étaient restés dans l'index Packwiz malgré le retrait des `.pw.toml`.

Tout est désormais nettoyé du côté de l'orchestration native Packwiz. **Attention :** Le client de test local de l'Agent 00 doit subir une synchronisation complète et propre (suppression de l'ancien dossier `mods/` du client avant la mise à jour via Packwiz) pour éviter que les anciens `.jar` (comme `geckoanimfix`) ne persistent localement.
