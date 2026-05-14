---
description: # Data Collection Workflow
---



## Description
This workflow governs the collection of raw data required for the Lucky World Invasion project, specifically Discord crash logs and community user data.

## Phase 1: Crash Log Harvesting
**Assignee:** User / Python Script (`discord_harvester.py`)
**Goal:** Extract `.txt` crash reports from Discord.

### Steps:
1. Run the Python harvester script.
2. Ensure files are saved to `E:\WORKS\luckyworldinvasion\crash_reports\`.
3. Verify files are not empty and contain valid stack traces.
4. Issue command: `/submit crash_reports`

## Phase 2: Community Data Tracking
**Assignee:** Subagent 4 (Community Data Tracker) / User
**Goal:** Maintain a database of users reporting issues.

### Steps:
1. Initialize `E:\WORKS\luckyworldinvasion\UsData.json`.
2. Extract Usernames, Discord Tags, and Roles from the Discord server.
3. Correlate users with the crash reports they submitted.
4. Save the structured JSON data.
5. Issue command: `/submit UsData.json`
