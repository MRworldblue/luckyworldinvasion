# Agent 7 - Hardcore Dev Review

## Mission Status
**Status:** [REVIEW]

## Executed Actions
1. **[FINISHED]** Reviewed `Lucky_world_invasion_hardcoreweb.md` specifications.
2. **[FINISHED]** Initialized `hardcore_project/` directory.
3. **[FINISHED]** Created initial project roadmap (`hardcore_project/roadmap.md`) and dependencies list (`hardcore_project/dependencies.md`).
4. **[FINISHED]** Generated this architectural plan for review.

## Architectural Plan: Lucky World Invasion - Hardcore Mode

### Objective
To transform the current Lucky World Invasion modpack into a strictly Hardcore, vanilla-aligned experience with increased difficulty, while retaining core identity (Lucky Blocks) and Quality of Life improvements.

### 1. Modpack Base Synchronization
- **Action:** Branch off the stable v2.x server/client base.
- **Tools:** Packwiz for dependency handling and version control.

### 2. Mod Purging & Cleanup
- **Target:** Remove mods that diverge from vanilla progression.
- **Specific Removals:**
  - `tacz` (Guns & Ammunition)
  - `touhou_little_maid` (Companions)
  - `waystones` (Teleportation)
  - Mushroom Kingdom dimension and associated generation mods.
- **Action:** Delete these from the `mods/` folder and `packwiz` index. Remove any KubeJS scripts or configs explicitly referencing them.

### 3. Core Mechanics Adjustments (KubeJS / Configs)
- **Hardcore Lock:** Modify `server.properties` and default world generation settings (`defaultconfigs` / `global_data`) to lock the world to Hardcore mode on creation.
- **Lucky Block Distribution:**
  - Update KubeJS loot tables and worldgen scripts.
  - Re-assign Lucky Blocks previously exclusive to the Mushroom Kingdom to spawn within the Overworld at balanced Y-levels and frequencies.
- **Difficulty Scaling:** Introduce appropriate difficulty scaling (e.g., via In Control! or modifying base mob attributes) to ensure the vanilla experience remains highly challenging.

### 4. Quality of Life (QoL) Preservation
- **Retention:** Keep `sophisticatedbackpacks` and similar non-intrusive inventory management tools.
- **Action:** Verify their configs do not trivialize the new hardcore difficulty (e.g., restricting certain overpowered upgrades).

### 5. Verification & Testing Strategy
- **Static Analysis:** Ensure no broken references in KubeJS after the removal of the targeted mods.
- **Worldgen Testing:** Launch a test instance to verify Overworld Lucky Block spawns and confirm the absence of the Mushroom Kingdom.
- **Stress Testing:** Validate stability during prolonged Hardcore survival to ensure no unexpected crashes.

## Next Steps
Awaiting supervisor approval (`done`) to proceed with executing the Mod Purging and Configuration phases.
