# 📋 Registre des Agents — Lucky World Invasion

> Équipe permanente. Chaque agent a un **métier**, pas un numéro de tâche jetable.

---

## 🚦 Ordre d'exécution actuel

```
Agent 1 (DevOps)  ──────►  Agent 2 (Release)  ──────►  Agent 4 (Intégration)
                  ├──────►  Agent 3 (Docs)              (quand un drop arrive)
                  └──────►  Agent 5 (QA)
```

| Étape | Agent | Fichier à copier-coller | Bloqué par |
|-------|-------|------------------------|------------|
| **1** | Agent 1 — DevOps Engineer | `.agents/Agent1_DevOps_Engineer.md` | Rien — **lancer maintenant** |
| **2a** | Agent 2 — Release Manager | `.agents/Agent2_Release_Manager.md` | Agent 1 terminé |
| **2b** | Agent 3 — Technical Writer | `.agents/Agent3_Technical_Writer.md` | Agent 1 terminé (parallèle avec 2) |
| **2c** | Agent 5 — QA Engineer | `.agents/Agent5_QA_Engineer.md` | Agent 1 terminé (parallèle avec 2+3) |
| **3** | Agent 4 — Integration Engineer | `.agents/Agent4_Integration_Engineer.md` | Agents 2+3 terminés + drop reçu |

---

## 👥 L'Équipe

| # | Métier | Scope | Statut |
|---|--------|-------|--------|
| 1 | **DevOps Engineer** | Structure repo, .gitignore, CI local, déploiement | 🟢 Prêt |
| 2 | **Release Manager** | Git, GitHub, branches, tags, versioning, publication | 🟡 Bloqué |
| 3 | **Technical Writer** | README, CONTRIBUTING, ARCHITECTURE, changelogs | 🟡 Bloqué |
| 4 | **Integration Engineer** | Drops contributeurs, imports Packwiz, feature branches | ⚪ Futur |
| 5 | **QA Engineer** | Crash analysis, bug triage, scripts de vérification | 🟡 Bloqué |

---

## 📁 Fichiers

```
.agents/
├── Agent1_DevOps_Engineer.md
├── Agent2_Release_Manager.md
├── Agent3_Technical_Writer.md
├── Agent4_Integration_Engineer.md
├── Agent5_QA_Engineer.md
└── REGISTRY.md                ← ce fichier
```
