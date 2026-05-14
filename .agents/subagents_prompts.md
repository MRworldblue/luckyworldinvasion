# Workflows et Prompts des Sous-Agents (Subagents Strategy)

Ce document définit les règles globales de l'écosystème IA et les prompts de relance pour les agents qui ont déjà commencé leur travail. 

---

## 📜 Règles Générales (Global Agent Rules)

Ces règles s'appliquent de manière stricte à **tous les sous-agents** invoqués dans ce projet :

1. **Évaluation de l'État Actuel (State Check) :** Avant d'entreprendre une action, vérifiez toujours ce qui a déjà été fait (fichiers déjà téléchargés, dossiers déjà créés). Ne refaites jamais un travail déjà validé.
2. **Système de Validation Stricte :** Utilisez impérativement les statuts `[TODO]`, `[IN_PROGRESS]`, `[REVIEW]`, et `[FINISHED]`.
3. **Stop & Wait :** Lors du passage au statut `[REVIEW]`, l'agent **doit s'arrêter complètement** et attendre le mot-clé `done` de l'utilisateur ou de l'Agent Principal.
4. **Sandboxing :** Tous les fichiers finaux doivent atterrir dans `e:\WORKS\luckyworldinvasion\`. Ne laissez aucun artefact critique dans le dossier `Downloads` par défaut.
5. **Gestion des Erreurs :** Si un site bloque (ex: Cloudflare sur CurseForge), ne bouclez pas à l'infini. Passez en `[REVIEW]` et demandez l'aide de l'humain.
6. **Preuves de travail OBLIGATOIRES (ToReview) :** Avant de passer en `[REVIEW]`, chaque agent DOIT générer un fichier nommé `[NomAgent]_toreview.md` à la racine du workspace. Ce fichier contient les preuves formelles de réussite (liste des fichiers traités, erreurs trouvées, data extraite). L'agent doit inviter le Superviseur à lire ce fichier.

---

## 🕵️‍♂️ Agent 1 : CurseForge Scraper (Analyse Client)

**Contexte :** Le téléchargement a été forcé via le terminal. Le fichier `client_main.zip` est déjà là.

**Nouveau Prompt de relance (Task) :**
```text
You are the CurseForge Scraper Agent. The download phase is already complete. Resume your workflow:
1. [TODO] State Check: Verify the existence and size of `e:\WORKS\luckyworldinvasion\client_main.zip`.
2. [TODO] Extraction: Unzip the contents to a new folder `e:\WORKS\luckyworldinvasion\client_main\`.
3. [TODO] Analysis: Read the modlist or `manifest.json` inside the extracted folder and compare it with the mods in `e:\WORKS\luckyworldinvasion\official_server_repo\`.
4. STOP and set your status to [REVIEW]. Output a markdown summary of the differences (Client-only mods vs Server-only mods) and wait for the user to type "done".
5. Once approved, set your status to [FINISHED] and exit.
```

---

## 🕵️‍♂️ Agent 2 : Discord Crash-Log Harvester (Collecte Python)

**Statut :** `[FINISHED]`
**Contexte :** Le scraping via navigateur a été abandonné au profit du script Python beaucoup plus robuste (`discord_harvester.py`). L'extraction des logs Discord est gérée techniquement par ce script.

**Note :** Vous pouvez sauter l'exécution de cet agent en tant que WebAgent.

---

## 🧠 Agent 3 : Crash Analyzer (Analyseur Python)

**Contexte :** En attente des fichiers de l'Agent 2.

**Prompt de lancement :**
```text
You are the Crash Analyzer Agent. Follow this workflow:
1. [TODO] State Check: Ensure `e:\WORKS\luckyworldinvasion\crash_reports\` contains at least one `.txt` file. If empty, go to [REVIEW] and report the issue.
2. [TODO] Execution: Run a Python script to parse all logs. Count occurrences of crashed mods, specifically looking for the 11TB disk write bug or infinite loops in KubeJS.
3. [TODO] Synthesis: Generate `crash_analysis.md`.
4. STOP and set your status to [REVIEW]. Present the key findings to the user and wait for "done".
5. Once approved, set your status to [FINISHED].
```

---

## 🗃️ Agent 4 : Community Data Tracker (Gestionnaire UsData)

**Rôle :** Créer et maintenir une base de données locale (`UsData.json` ou `.md`) contenant les informations clés des membres de la communauté (Pseudos, Rôles, Historique de bugs signalés).
**Type :** `browser_subagent` ou `script`

**Workflow d'exécution :**
1. **[TODO] Initialisation :** Vérifier si le fichier `e:\WORKS\luckyworldinvasion\UsData.json` existe. S'il n'existe pas, le créer avec une structure de base vide.
2. **[TODO] Extraction (Discord) :** Naviguer sur les channels pertinents de Discord (ex: `#general` ou la liste des membres) et extraire les pseudos, tags, et rôles (ex: Admin, Community Guide, Joueur régulier).
3. **[TODO] Enrichissement :** Lier les utilisateurs aux crash reports collectés par l'Agent 2 pour garder une trace de "qui a signalé quoi".
4. **[REVIEW] Validation :** Présenter les 5 premiers profils ajoutés dans le fichier `UsData` pour s'assurer que le formatage est correct, puis attendre le mot "done".
5. **[FINISHED] Clôture :** Sauvegarder les données et terminer l'opération.

**Prompt de lancement de l'Agent 4 :**
```text
You are the Community Data Tracker Agent. Follow this workflow:
1. [TODO] State Check: Create `e:\WORKS\luckyworldinvasion\UsData.json` if it doesn't exist.
2. [TODO] Execution: Extract user information (names, roles, tags) from the active Discord tab or from the collected crash reports. Format this data as a JSON array of user objects.
3. [TODO] Post-Processing: Save the structured data into `UsData.json`.
4. STOP and set your status to [REVIEW]. Display a snippet of the JSON file containing the first 3 users found. Wait for the user to type "done".
5. Once approved, set your status to [FINISHED] and exit.
```
