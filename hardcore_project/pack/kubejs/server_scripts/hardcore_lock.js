/**
 * Hardcore Lock Script
 * Ce script force la difficulté à "Difficile" et bloque le monde pour simuler
 * le mode Hardcore si le joueur n'a pas sélectionné Hardcore à la création.
 */

ServerEvents.loaded(event => {
    let server = event.server;
    
    // Force la difficulté à Hard et la verrouille
    server.setDifficulty('hard');
    server.setDifficultyLocked(true);
});

// Simulation du Hardcore pour le Solo
PlayerEvents.respawned(event => {
    let server = event.server;
    
    // Si le serveur/monde n'est pas nativement en mode Hardcore
    if (server.worldData && !server.worldData.isHardcore()) {
        let player = event.player;
        
        // Passer le joueur en mode Spectateur
        player.setGameMode('spectator');
        
        // Afficher un message de fin de partie
        player.tell(Text.red("☠ Vous êtes mort. Ce modpack est conçu pour être joué en Hardcore."));
        player.tell(Text.gray("Vous êtes maintenant en mode Spectateur. Fin de partie."));
    }
});
