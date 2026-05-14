# 🛠️ MISSION DIRECTIVE : AGENT 11 (DÉBOGAGE HARDCORE V1)

## 📌 Contexte
Suite à la création du modpack "Hardcore V1" (version 2.7.2/2.6.1), le client crashe au lancement. Le Superviseur Antigravity (Agent 00) a analysé les logs (fml-crash) et identifié des dépendances orphelines et des incompatibilités causées par la purge de l'Agent 8.

## 🎯 Objectifs de la Mission
Ton but est de nettoyer les mods restants qui causent le crash, de mettre à jour l'index Packwiz, et de t'assurer que le modpack compile correctement.

### Tâche 1 : Purge des dépendances `tacz` orphelines
Lors de l'étape précédente, le mod `tacz` a été supprimé pour respecter la vision Hardcore. Cependant, des addons sont restés :
- Supprime **`gunsmithlib`** (ex: `gunsmithlib-forge-...jar`) du dossier `hardcore_project/pack/mods/` ou via Packwiz.
- Supprime **`apotheosis_modern_ragnarok`** (ex: `apotheosis_modern_ragnarok-forge-...jar`) du dossier `hardcore_project/pack/mods/` ou via Packwiz.

### Tâche 2 : Résolution du conflit GeckoLib
Le crash log indique : `Mod geckolib only supports geckoanimfix 9.thismodbreaksgeckolibremoveit or above`.
- Supprime le mod **`geckoanimfix`** qui est explicitement blacklisté/incompatible avec la version actuelle de `geckolib`.

### Tâche 3 : Synchronisation Packwiz
- Exécute la commande Packwiz pour rafraîchir l'index du modpack dans le répertoire `hardcore_project/pack/` (ex: `packwiz refresh`).
- Assure-toi que les fichiers supprimés sont bien enlevés de l'index (`index.toml`).

### Tâche 4 : Génération du Rapport
- Crée un fichier `Agent11_toreview.md` à la racine de `e:\WORKS\luckyworldinvasion\` détaillant les mods supprimés, les commandes exécutées et le statut final `[REVIEW]`.
- N'exécute pas le jeu toi-même. Le Directeur s'en chargera une fois ton rapport validé.

## 🚨 Règles strictes
- Travaille uniquement dans `e:\WORKS\luckyworldinvasion\hardcore_project\pack\`.
- Respecte le Protocole d'Orchestration Native : génère un rapport final clair pour le Superviseur.
- Ne rajoute aucun mod, contente-toi de retirer ceux qui posent problème.

---
**STATUT ATTENDU EN FIN DE MISSION :** `[REVIEW]` dans `Agent11_toreview.md`
