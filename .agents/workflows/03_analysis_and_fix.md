---
description: # Analysis & Bug Fixing Workflow
---

# Analysis & Bug Fixing Workflow

## Description
This workflow covers the analysis of collected data to identify critical bugs (such as the 11TB disk write issue) and the subsequent fixing process.

## Phase 1: Crash Analysis
**Assignee:** Data Analyst Agent / User Python Script
**Prerequisite:** Approved `crash_reports` from Data Collection Workflow.

### Steps:
1. Parse all `.txt` files in `E:\WORKS\luckyworldinvasion\crash_reports\`.
2. Aggregate errors by Exception Type and Mod Name.
3. Specifically search for infinite loops (e.g., KubeJS) or massive I/O operations.
4. Generate a summary report at `E:\WORKS\luckyworldinvasion\crash_analysis.md`.
5. Issue command: `/submit crash_analysis.md`

## Phase 2: Server vs Client Diff
**Assignee:** Configuration Agent / User
**Prerequisite:** Official Server Repo cloned, Client `.zip` downloaded and extracted.

### Steps:
1. Extract `E:\WORKS\luckyworldinvasion\client_main.zip` to a temporary directory.
2. Compare the `mods/` directory of the client against the `official_server_repo/mods/`.
3. Identify discrepancies (mods missing on server, client-only mods like minimaps, etc.).
4. Generate `diff_report.md`.
5. Issue command: `/submit diff_report.md`
