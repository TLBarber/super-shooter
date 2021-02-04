namespace SpriteKind {
    export const powerup = SpriteKind.create()
    export const autofire_power = SpriteKind.create()
}
function normalfire () {
    if (setup_complete == 1) {
        projectile2 = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . 9 9 9 . . . . . 
            . . . . 9 9 9 9 9 5 9 . . . . . 
            . . . . . . . . 9 9 9 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, mySprite, 105, 0)
        projectile2.setFlag(SpriteFlag.AutoDestroy, true)
        music.pewPew.play()
        if (powerlevel >= 1) {
            projectile2.y += -5
            projectile2 = sprites.createProjectileFromSprite(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . 9 9 9 . . . . . 
                . . . . 9 9 9 9 9 5 9 . . . . . 
                . . . . . . . . 9 9 9 . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, mySprite, 105, 0)
            projectile2.setFlag(SpriteFlag.AutoDestroy, true)
            projectile2.y += 5
            if (powerlevel == 1) {
                powerup_counter += 1
                if (powerup_counter == 50) {
                    powerup_counter += -50
                    powerlevel += -1
                }
            }
        }
        if (powerlevel >= 2) {
            projectile2 = sprites.createProjectileFromSprite(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . 9 9 9 . . . . . 
                . . . . 9 9 9 9 9 5 9 . . . . . 
                . . . . . . . . 9 9 9 . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, mySprite, 105, 5)
            projectile2.y += 10
            projectile2.setFlag(SpriteFlag.AutoDestroy, true)
            projectile2 = sprites.createProjectileFromSprite(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . 9 9 9 . . . . . 
                . . . . 9 9 9 9 9 5 9 . . . . . 
                . . . . . . . . 9 9 9 . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, mySprite, 105, -5)
            projectile2.setFlag(SpriteFlag.AutoDestroy, true)
            projectile2.y += -10
            powerup_counter += 1
            if (powerup_counter == 250) {
                powerup_counter += -250
                powerlevel += -1
            }
        }
    }
}
function initialize_variables () {
    setup_complete = 0
    info.setLife(3)
    chests = 0
    spawn_rate = 1000
    powerlevel = 0
    shielded = 0
    speed = -20
    textSprite = textsprite.create("x" + convertToText(chests), 15, 5)
    textSprite.setIcon(img`
        . . b b b b b b b b b b b b . . 
        . b e 4 4 4 4 4 4 4 4 4 4 e b . 
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
        b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
        b e e 4 4 4 4 4 4 4 4 4 4 e e b 
        b e e e e e e e e e e e e e e b 
        b e e e e e e e e e e e e e e b 
        b b b b b b 5 5 5 5 b b b b b b 
        c b b b b b 5 b b 5 b b b b b c 
        c c c c c c 5 c c 5 c c c c c c 
        b e e e e e 5 5 5 5 e e e e e b 
        b e e e e e e e e e e e e e e b 
        b c e e e e e e e e e e e e c b 
        b b b b b b b b b b b b b b b b 
        . b b . . . . . . . . . . b b . 
        `)
    textSprite.setPosition(15, 20)
    autofire = 0
    projectile_count = 0
    firedelay = 10
    delaycounter = 0
    powerup_counter = 0
}
function holdFire () {
    if (autofire == 1) {
        rapidfirelaser = sprites.createProjectileFromSprite(assets.image`lazer`, mySprite, 105, 0)
        projectile2.setFlag(SpriteFlag.AutoDestroy, true)
        projectile_count += 1
        music.magicWand.play()
        autofire_indicator.setText("x" + convertToText(1000 - projectile_count * 4))
        if (projectile_count >= 250) {
            projectile_count = 0
            autofire = 0
            autofire_indicator.destroy()
        }
    } else if (firedelay == delaycounter) {
        normalfire()
        delaycounter = 0
    } else {
        delaycounter += 1
    }
}
function makeEnemies () {
    if (game.runtime() > 60000) {
        makeShark()
    }
    if (game.runtime() > 120000) {
        makeShark()
        makeShark()
    }
    if (game.runtime() > 180000) {
        makeShark()
        makeShark()
        makeShark()
    }
    makeShark()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.autofire_power, function (sprite, otherSprite) {
    pickupRapidFire(otherSprite)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    normalfire()
})
function pickupRapidFire (powerup: Sprite) {
    if (autofire == 0) {
        powerup.destroy(effects.smiles, 200)
        music.magicWand.play()
        autofire += 1
        autofire_indicator = textsprite.create("x1000")
        autofire_indicator.setIcon(img`
            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
            6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
            6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
            6 9 6 6 9 9 c c 6 9 9 9 6 6 9 6 
            6 6 6 9 9 9 9 c 6 6 9 9 9 6 6 6 
            6 6 9 9 9 9 9 9 6 6 9 9 9 9 6 6 
            6 9 9 9 6 6 6 6 9 6 9 9 c 9 9 6 
            6 9 c 6 6 6 9 9 9 6 9 c c c 9 6 
            6 9 c c c 9 6 9 9 9 6 6 6 c 9 6 
            6 9 9 c 9 9 6 9 6 6 6 6 9 9 9 6 
            6 6 9 9 9 9 6 6 9 9 9 9 9 9 6 6 
            6 6 6 9 9 9 6 6 c 9 9 9 9 6 6 6 
            6 9 6 6 9 9 9 6 c c 9 9 6 6 9 6 
            6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
            6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
            `)
        autofire_indicator.setPosition(55, 8)
    } else {
        music.magicWand.play()
        powerup.destroy(effects.smiles, 200)
        autofire_indicator.setText("x1000")
        projectile_count = 0
    }
}
function pickupPowerup (player2: Sprite, powerup: Sprite) {
    powerup.destroy(effects.smiles, 200)
    music.jumpUp.play()
    powerlevel += 1
    if (powerlevel == 3) {
        shieldup()
        powerlevel += -1
    } else {
        powerup_counter = 0
    }
}
function enemyGetsShot (projectile: Sprite, enemy: Sprite) {
    projectile.destroy(effects.fire, 200)
    statusbars.getStatusBarAttachedTo(StatusBarKind.Health, enemy).value += randint(-1, -2)
    if (statusbars.getStatusBarAttachedTo(StatusBarKind.Health, enemy).value <= 0) {
        statusbars.getStatusBarAttachedTo(StatusBarKind.Health, enemy).spriteAttachedTo().destroy(effects.fire, 200)
        music.jumpDown.play()
        info.changeScoreBy(10)
        if (info.score() % 100 == 0) {
            speed += -20
        }
    }
}
function shieldup () {
    mySprite.setImage(img`
        ....................
        ....................
        ....................
        ................9...
        ..222222222222...99.
        ..222222222222...98.
        ..222222222222...98.
        ..222522225222...98.
        ..222222222222...98.
        ..222222222222...98.
        ..222222222222...98.
        ..222222222222...98.
        999999999999999..98.
        9999999999999999.98.
        9999999999999999.98.
        999999999999999..99.
        ................9...
        ....................
        ....................
        ....................
        `)
    shielded = 1
}
function makePowerups () {
    if (Math.percentChance(10)) {
        mySprite3 = sprites.create(img`
            . . b b b b b b b b b b b b . . 
            . b e 4 4 4 4 4 4 4 4 4 4 e b . 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
            b e e 4 4 4 4 4 4 4 4 4 4 e e b 
            b e e e e e e e e e e e e e e b 
            b e e e e e e e e e e e e e e b 
            b b b b b b 5 5 5 5 b b b b b b 
            c b b b b b 5 b b 5 b b b b b c 
            c c c c c c 5 c c 5 c c c c c c 
            b e e e e e 5 5 5 5 e e e e e b 
            b e e e e e e e e e e e e e e b 
            b c e e e e e e e e e e e e c b 
            b b b b b b b b b b b b b b b b 
            . b b . . . . . . . . . . b b . 
            `, SpriteKind.Food)
        mySprite3.x = 160
        mySprite3.y = randint(20, 100)
        mySprite3.setVelocity(-30, 0)
        mySprite3.setFlag(SpriteFlag.AutoDestroy, false)
        makeShark()
        makeShark()
    } else if (powerlevel <= 2 && Math.percentChance(10)) {
        if (powerlevel == 2 && shielded == 0) {
            mySprite4 = sprites.create(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . 6 6 6 5 5 6 6 6 . . . . 
                . . . 7 7 7 7 6 6 6 6 6 6 . . . 
                . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
                . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
                . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
                . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
                . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
                . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
                . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
                . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
                . . . 6 8 8 8 8 8 8 8 8 6 . . . 
                . . . . 6 6 8 8 8 8 6 6 . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, SpriteKind.powerup)
            animation.runImageAnimation(
            mySprite4,
            [img`
                . . . . . . . . . . . . . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . 6 6 6 5 5 6 6 6 . . . . 
                . . . 7 7 7 7 6 6 6 6 6 6 . . . 
                . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
                . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
                . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
                . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
                . 6 6 7 7 8 8 6 6 6 6 6 8 6 6 . 
                . 6 8 7 7 8 8 6 6 6 6 8 6 6 6 . 
                . . 6 8 7 7 8 6 6 6 6 8 6 6 . . 
                . . 6 8 8 7 8 8 6 6 6 6 6 6 . . 
                . . . 6 8 8 8 8 8 8 8 8 6 . . . 
                . . . . 6 6 8 8 8 8 6 6 . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . . . . . . . . . . . . . 
                `,img`
                . . . . . . . . . . . . . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . 6 6 6 5 5 6 6 6 . . . . 
                . . . 7 7 7 7 6 6 6 6 6 6 . . . 
                . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
                . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
                . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
                . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
                . 6 6 7 7 8 8 6 6 6 6 6 8 6 6 . 
                . 6 8 7 7 8 8 6 6 6 6 8 6 6 6 . 
                . . 6 8 7 7 8 6 8 6 8 8 6 6 . . 
                . . 6 8 8 7 8 8 6 8 6 6 6 6 . . 
                . . . 6 8 8 8 8 8 8 8 8 6 . . . 
                . . . . 6 6 8 8 8 8 6 6 . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . . . . . . . . . . . . . 
                `,img`
                . . . . . . . . . . . . . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . 6 6 6 5 5 6 6 6 . . . . 
                . . . 7 7 7 7 6 6 6 6 6 6 . . . 
                . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
                . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
                . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
                . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
                . 6 6 7 7 8 8 6 8 8 6 6 8 6 6 . 
                . 6 8 7 7 8 8 6 8 6 6 8 6 6 6 . 
                . . 6 8 7 7 8 6 8 6 8 8 6 6 . . 
                . . 6 8 8 7 8 8 6 8 6 6 6 6 . . 
                . . . 6 8 8 8 8 8 8 8 8 6 . . . 
                . . . . 6 6 8 8 8 8 6 6 . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . . . . . . . . . . . . . 
                `],
            500,
            false
            )
        } else {
            mySprite4 = sprites.create(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . 5 5 5 5 . . . . . . 
                . . . . 5 5 5 5 5 5 5 5 . . . . 
                . . . 5 5 5 5 5 5 5 5 5 5 . . . 
                . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                . . . 5 5 5 5 5 5 5 5 5 5 . . . 
                . . . . 5 5 5 5 5 5 5 5 . . . . 
                . . . . . . 5 5 5 5 . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, SpriteKind.powerup)
        }
        mySprite4.x = 160
        mySprite4.y = randint(20, 100)
        mySprite4.setVelocity(-50, 0)
        mySprite4.setFlag(SpriteFlag.AutoDestroy, false)
    }
    if (Math.percentChance(1)) {
        autofire_sprite = sprites.create(img`
            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
            6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
            6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
            6 9 6 6 9 9 c c 6 9 9 9 6 6 9 6 
            6 6 6 9 9 9 9 c 6 6 9 9 9 6 6 6 
            6 6 9 9 9 9 9 9 6 6 9 9 9 9 6 6 
            6 9 9 9 6 6 6 6 9 6 9 9 c 9 9 6 
            6 9 c 6 6 6 9 9 9 6 9 c c c 9 6 
            6 9 c c c 9 6 9 9 9 6 6 6 c 9 6 
            6 9 9 c 9 9 6 9 6 6 6 6 9 9 9 6 
            6 6 9 9 9 9 6 6 9 9 9 9 9 9 6 6 
            6 6 6 9 9 9 6 6 c 9 9 9 9 6 6 6 
            6 9 6 6 9 9 9 6 c c 9 9 6 6 9 6 
            6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
            6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
            `, SpriteKind.autofire_power)
        autofire_sprite.x = 160
        autofire_sprite.setVelocity(-50, 0)
        autofire_sprite.setFlag(SpriteFlag.AutoDestroy, false)
    }
}
function pickupChest (chest: Sprite) {
    chest.destroy(effects.hearts, 200)
    music.baDing.play()
    chests += 1
    textSprite.setText("x" + convertToText(chests))
    if (chests == 10) {
        game.over(true)
    }
}
controller.A.onEvent(ControllerButtonEvent.Repeated, function () {
    holdFire()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    pickupChest(otherSprite)
})
function createPlayer () {
    mySprite = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
        . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
        . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
        . . 2 2 2 5 2 2 2 2 5 2 2 2 . . 
        . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
        . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
        . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
        . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 . 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 . 
        `, SpriteKind.Player)
    mySprite.x = 50
    mySprite.setStayInScreen(true)
    animation.runMovementAnimation(
    mySprite,
    animation.animationPresets(animation.easeLeft),
    1000,
    false
    )
    music.playMelody("G B A B C5 B A B ", 246)
    controller.moveSprite(mySprite)
}
function enemyCollision (player2: Sprite, enemy: Sprite) {
    if (shielded > 0) {
        enemy.destroy(effects.fire, 200)
        shielded = 0
        mySprite.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
            . . 2 2 2 5 2 2 2 2 5 2 2 2 . . 
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 . 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 . 
            `)
    } else {
        enemy.destroy(effects.fire, 200)
        info.changeLifeBy(-1)
        player2.destroy(effects.fire, 200)
        music.wawawawaa.play()
        if (info.life() > 0) {
            if (0 < powerlevel) {
                powerlevel += -1
            }
            if (game.ask("Ready?")) {
                mySprite = sprites.create(img`
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                    . . 2 2 2 5 2 2 2 2 5 2 2 2 . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 . 
                    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 . 
                    `, SpriteKind.Player)
                mySprite.x = 15
                mySprite.setStayInScreen(true)
                controller.moveSprite(mySprite)
            } else {
                game.over(false, effects.melt)
            }
        } else {
            game.over(false, effects.melt)
        }
    }
}
function makeShark () {
    mySprite2 = sprites.create(img`
        .............ccfff..............
        ...........ccddbcf..............
        ..........ccddbbf...............
        ..........fccbbcf...............
        .....fffffccccccff.........ccc..
        ...ffbbbbbbbcbbbbcfff....ccbbc..
        ..fbbbbbbbbcbcbbbbcccff.cdbbc...
        ffbbbbbbffbbcbcbbbcccccfcdbbf...
        fbcbbb11ff1bcbbbbbcccccffbbf....
        fbbb11111111bbbbbcccccccbbcf....
        .fb11133cc11bbbbcccccccccccf....
        ..fccc31c111bbbcccccbdbffbbcf...
        ...fc13c111cbbbfcddddcc..fbbf...
        ....fccc111fbdbbccdcc.....fbbf..
        ........ccccfcdbbcc........fff..
        .............fffff..............
        `, SpriteKind.Enemy)
    statusbar = statusbars.create(20, 4, StatusBarKind.Health)
    statusbar.max = 2
    statusbar.attachToSprite(mySprite2, 5, 0)
    mySprite2.x = 160
    mySprite2.y = randint(20, 100)
    mySprite2.setVelocity(randint(speed / 2, speed), randint(-2, 2))
    mySprite2.setFlag(SpriteFlag.AutoDestroy, true)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.powerup, function (sprite, otherSprite) {
    pickupPowerup(sprite, otherSprite)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    enemyGetsShot(sprite, otherSprite)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    enemyCollision(sprite, otherSprite)
})
let statusbar: StatusBarSprite = null
let mySprite2: Sprite = null
let autofire_sprite: Sprite = null
let mySprite4: Sprite = null
let mySprite3: Sprite = null
let autofire_indicator: TextSprite = null
let rapidfirelaser: Sprite = null
let delaycounter = 0
let firedelay = 0
let projectile_count = 0
let autofire = 0
let textSprite: TextSprite = null
let speed = 0
let shielded = 0
let spawn_rate = 0
let chests = 0
let powerup_counter = 0
let powerlevel = 0
let mySprite: Sprite = null
let projectile2: Sprite = null
let setup_complete = 0
initialize_variables()
effects.starField.startScreenEffect()
scene.setBackgroundColor(15)
createPlayer()
setup_complete = 1
game.onUpdateInterval(spawn_rate, function () {
    makeEnemies()
    makePowerups()
})
