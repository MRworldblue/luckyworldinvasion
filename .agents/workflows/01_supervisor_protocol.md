---
description: # Supervisor Protocol Workflow (V2 - Auto-Execution)
---


## Description
This workflow defines the fully automated orchestration of the project. The AI Supervisor (Antigravity) is responsible for taking all actions directly via its tools (`run_command`, `browser_subagent`, `write_to_file`).

## Rôle de l'Utilisateur (Directeur Technique)
Le Directeur dirige l'orchestration via des commandes de délégation. Il donne l'ordre au Superviseur, qui l'exécute ensuite.
- **Commande de lancement :** `/do [NomAgent] [Action]`
- **Exemple :** `/do Agent6 packwiz_init`

## Flux de Commande Strict (NO AUTO-EXECUTION)
`Directeur -> Superviseur -> Génération du Prompt -> Agent (Exécuté par l'humain) -> Preuve (.toreview) -> Directeur -> Superviseur (/review)`

**RÈGLE ABSOLUE POUR LE SUPERVISEUR (AGENT 00) :**
Le Superviseur **NE DOIT JAMAIS** utiliser `run_command` ou éditer les fichiers de code lui-même. 
Quand le Directeur tape `/do AgentX`, le Superviseur doit UNIQUEMENT répondre en générant le prompt ou le fichier d'instructions exact que l'Agent X devra exécuter.
Ensuite, le Superviseur demande au Directeur : *"Agent X a terminé et généré son fichier toReview ? Tape /review [NomFichier] pour que je l'analyse."*

## Workflow Actuel : Data Collection
- Le Superviseur lance le script de récolte Python.
- Le Superviseur analyse le dossier `crash_reports`.
- Le Superviseur lance l'Analyseur de logs.
