# Agent 8 - Hardcore Purger Review

## Mission Status
**Status:** [REVIEW]

## Executed Actions
1. **[FINISHED]** Navigated to `hardcore_project/pack/` and copied the base modpack from `lucky_world_invasion_2.0/`.
2. **[FINISHED]** Removed the following mods from the packwiz index and deleted their configurations:
   - `tacz` and all related TACZ add-ons (`timeless-and-classics-zero`, `third-person-shooting`, `tacz-addon`, `tacz-bullet-proof-enchant-add-on`, `tacz-gucci-vuitton-attachments`, `tacz-js`, `tacz-lesraisins-tactical-equipements`)
   - `touhou_little_maid` and related add-ons (`maid-useful-tasks`, `maidsoul-kitchen`, `youkais-homecoming`)
   - `waystones`
   - `super-block-world` (Mushroom Kingdom dimension and related items)
3. **[FINISHED]** Purged all KubeJS scripts referencing these deleted mods:
   - Modified `startup_scripts/mob_effect_event.js` to remove `touhou_little_maid:maid` references.
   - Modified `server_scripts/entity_events.js` to remove Touhou Maid custom logic and interactions.
   - Modified `server_scripts/lucky_block_event.js` to remove `super_block_world:launch_star` and `super_block_world:power_star`.
   - Modified `server_scripts/loots.js` to remove the modified loot pool for `super_block_world:brick_fortress`.
   - Replaced `"biomes": "super_block_world:gritzy_desert"` with `"minecraft:desert"` in `data/legendary_monsters/worldgen/structure/ruined_pyramid.json`.
   - Deleted KubeJS directories heavily tied to removed mods: `data/trisdyna`, `data/emxarms`, `assets/super_block_world`, and `data/puresuffering/invasion_types/octoomba_game.json`.
4. **[FINISHED]** Refreshed the packwiz index.
5. **[REVIEW]** Awaiting validation to finalize Step 2 of the Hardcore Plan.

## Summary of Deleted Files
- `mods/tacz*.pw.toml`
- `mods/timeless-and-classics-zero.pw.toml`
- `mods/third-person-shooting.pw.toml`
- `mods/touhou*.pw.toml`
- `mods/maid*.pw.toml`
- `mods/youkais-homecoming.pw.toml`
- `mods/waystones.pw.toml`
- `mods/super-block-world.pw.toml`
- `tacz/` directory.
- `kubejs/data/trisdyna/` directory.
- `kubejs/data/emxarms/` directory.
- `kubejs/assets/super_block_world/` directory.
- `kubejs/data/puresuffering/invasion_types/octoomba_game.json`
