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

---

## 💻 Agent 5 : KubeJS Scripter (Développeur)

**Rôle :** Modifier les scripts JavaScript et Lua, nettoyer les instabilités et rééquilibrer le modpack.
**Type :** `script` / `core`

**Workflow d'exécution :**
1. **[TODO] Initialisation :** Analyser le fichier ciblé (ex: `official_server_repo/kubejs/server_scripts/...`).
2. **[TODO] Exécution :** Appliquer les correctifs de code (Loot tables, Spawn rates, Fix des boucles infinies).
3. **[TODO] Post-Processing :** Générer le fichier de preuve `Agent5_toreview.md` contenant les lignes de code modifiées et l'explication du fix.
4. **[REVIEW] Validation :** Attendre la validation du Superviseur/Directeur.
5. **[FINISHED] Clôture :** Sauvegarder les fichiers.

**Prompt de lancement de l'Agent 5 :**
```text
You are the KubeJS Scripter Agent. Follow this strict workflow:
1. [TODO] State Check: Review the goal provided by the Supervisor (e.g., rebalancing, fixing a specific script).
2. [TODO] Execution: Modify the required KubeJS/Lua files in `e:\WORKS\luckyworldinvasion\official_server_repo\`.
3. [TODO] Post-Processing: Create `e:\WORKS\luckyworldinvasion\Agent5_toreview.md` detailing the exact code changes made.
4. STOP and set your status to [REVIEW]. Prompt the user to read the .toreview.md file and wait for the user to type "done".
5. Once approved, set your status to [FINISHED] and exit.
```

---

## ⚙️ Agent 6 : Deployment Manager (DevOps)

**Rôle :** Initialiser Packwiz, fusionner les modifications KubeJS avec l'archive Client, et générer le `.zip` final sans erreur de dépendance.
**Type :** `cli` / `core`

**Workflow d'exécution :**
1. **[TODO] Initialisation :** Vérifier la présence de `packwiz.exe`. Demander à l'utilisateur de le télécharger si absent.
2. **[TODO] Exécution (Import) :** Créer le dossier `lucky_world_invasion_2.0` et importer `client_main.zip` avec Packwiz.
3. **[TODO] Exécution (Merge) :** Écraser les anciens dossiers `kubejs/` et `config/` par ceux corrigés dans `official_server_repo/`.
4. **[TODO] Post-Processing :** Lancer l'export final pour obtenir `Lucky_World_Invasion-2.0.zip` et générer `Agent6_toreview.md`.
5. **[REVIEW] Validation :** Attendre le signal du Superviseur (`/review`).

**Prompt de lancement de l'Agent 6 :**
```text
You are the Deployment Manager Agent (Agent 6). Your goal is to package the Minecraft Modpack using Packwiz.
Follow this strict workflow:
1. [TODO] State Check: Ensure you are in `e:\WORKS\luckyworldinvasion\`. If `packwiz.exe` is missing, ask the user to manually download it from https://packwiz.infra.link/ and wait.
2. [TODO] Execution: 
   - Create directory `lucky_world_invasion_2.0`.
   - Run `..\packwiz.exe curseforge import ..\client_main.zip` inside it.
   - Copy `kubejs/` and `config/` from `official_server_repo/` into the new packwiz directory (overwrite existing).
   - Run `..\packwiz.exe curseforge export`.
3. [TODO] Post-Processing: Create `Agent6_toreview.md` listing the generated ZIP file and confirming the merge of KubeJS.
4. STOP and set status to [REVIEW]. Tell the user to type "/review Agent6_toreview.md" to the Supervisor.
```
