---
trigger: always_on
---

Ces règles s'appliquent de manière stricte à **tous les sous-agents** invoqués dans ce projet :
1. **Évaluation de l'État Actuel (State Check) :** Avant d'entreprendre une action, vérifiez toujours ce qui a déjà été fait (fichiers déjà téléchargés, dossiers déjà créés). Ne refaites jamais un travail déjà validé.
2. **Système de Validation Stricte :** Utilisez impérativement les statuts `[TODO]`, `[IN_PROGRESS]`, `[REVIEW]`, et `[FINISHED]`.
3. **Stop & Wait :** Lors du passage au statut `[REVIEW]`, l'agent **doit s'arrêter complètement** et attendre le mot-clé `done` de l'utilisateur ou de l'Agent Principal.
4. **Sandboxing :** Tous les fichiers finaux doivent atterrir dans `e:\WORKS\luckyworldinvasion\`. Ne laissez aucun artefact critique dans le dossier `Downloads` par défaut.
5. **Gestion des Erreurs :** Si un site bloque (ex: Cloudflare sur CurseForge), ne bouclez pas à l'infini. Passez en `[REVIEW]` et demandez l'aide de l'humain.