// Hardcore Enforcer
ServerEvents.loaded(event => {
    event.server.runCommandSilent('/difficulty hard');
});

PlayerEvents.loggedIn(event => {
    if (event.server.worldData && !event.server.worldData.isHardcore()) {
        event.player.tell(Text.of("⚠️ [WARNING] This modpack is designed exclusively for Hardcore mode! It is highly recommended to play on Hardcore.").red());
    }
});
