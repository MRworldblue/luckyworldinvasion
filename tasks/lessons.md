# Lessons Learned & Anti-Patterns

## 1. KubeJS Global Scope in Forge Events
- **Pattern/Mistake:** Defining a `global.FunctionName = event => {}` in `server_scripts` and trying to call it from `ForgeEvents.onEvent(...)` in `startup_scripts`. 
- **Consequence:** Causes a `TypeError: Cannot find function` during gameplay because `startup_scripts` load in a different context/timing than `server_scripts`, and `global` properties might not cross over cleanly when handling native Forge events.
- **Rule/Fix:** Register `ForgeEvents.onEvent` directly inside `server_scripts` if the event is a server-side/in-game event (like `LivingHurtEvent`). Avoid unnecessary cross-script `global` wrappers for event listeners.

## 2. CurseForge Profile Updates
- **Pattern/Mistake:** Updating an existing CurseForge profile with a new `.zip` from Packwiz after deleting mods.
- **Consequence:** CurseForge does **not** delete old `.jar` files that are missing from the new ZIP's index. This leads to orphaned mods remaining in the `mods/` folder and causing crashes.
- **Rule/Fix:** For local testing, either create a completely new profile every time, or implement the **Packwiz Installer Bootstrapper** for automated, clean syncing.
