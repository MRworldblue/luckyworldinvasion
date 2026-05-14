StartupEvents.registry('mob_effect', (event) => {
    event.create('kubejs:lucky_shield')
        .color(0xff9d00)
        .beneficial()
        .effectTick((ett, lv) => {
            let { age, level, absorptionAmount } = ett;
            if (level.clientSide) return;
            if (age % 20 == 0) {
                let maxAmount = (lv + 1) * 5
                if (absorptionAmount < maxAmount) {
                    absorptionAmount = Math.min(maxAmount, absorptionAmount + (lv + 1) * 5)
                    ett.setAbsorptionAmount(absorptionAmount)
                }
            }
        })
        .modifyAttribute('minecraft:generic.armor_toughness', 'modify_armor_toughness', 0.01, 'multiply_base')
        .modifyAttribute('minecraft:generic.armor', 'modify_armor', 0.01, 'multiply_base')
        .createObject()
})
