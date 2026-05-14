# Agent 9: Mechanics Updater Review
**Status:** `[REVIEW]`

## 1. Hardcore Lock Implementation
*   **server.properties**:
    *   Set `hardcore=true`.
    *   Verified `difficulty=hard`.
*   **Singleplayer Global Configs (KubeJS)**:
    *   Created `hardcore_project/pack/kubejs/server_scripts/hardcore_lock.js` to automatically set the server difficulty to `hard` on server load via `/difficulty hard`.
    *   Added a login check (`PlayerEvents.loggedIn`) to verify `event.server.worldData.isHardcore()`. If it's not hardcore, it outputs a strict `[WARNING]` in chat notifying the player to recreate the world in Hardcore, since vanilla Minecraft singleplayer doesn't let mods easily force Hardcore mode *before* world creation without specific locked configs.

## 2. Lucky Block Distribution
*   Modified the `natural_gen.txt` generation configurations for Lucky Blocks across the `config/lucky/` and `addons/lucky/` directories.
*   **Dimension Fix**: Re-assigned `>super_block_world:mushroom_kingdom` tags to `>minecraft:overworld` allowing the blocks to spawn naturally in the Overworld.
*   **Structure Fixes**: Replaced references to purged Mushroom Kingdom blocks (`super_block_world:vanillate`, `gritzy_sand`, `hardstone`) with vanilla equivalents (`minecraft:dirt`, `minecraft:sand`, `minecraft:stone`) in the unlucky ruins structure generation to prevent missing block issues or crashes.
*   The frequency (`@chance`) remains at its default balanced value for vanilla overworld generation (e.g., `chance=50` to `chance=200` depending on the variant).

## 3. Difficulty Scaling Check
*   Verified KubeJS `difficulty_control.js` script. The logic that previously reduced a player's difficulty (`improvedmobs difficulty player ... add -x`) upon death is already commented out (`HARDCORE PATCH : Désactivation de la baisse de difficulté à la mort`). This ensures players cannot game the system by dying to lower difficulty, maintaining a punishing but fair difficulty curve.

Please review these changes before proceeding.
