namespace SpriteKind {
    export const powerup = SpriteKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    music.jumpUp.play()
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
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
    }
})
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
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    otherSprite.destroy(effects.hearts, 200)
    music.baDing.play()
    chests += 1
    textSprite.setText("x" + convertToText(chests))
    if (chests == 10) {
        game.over(true)
    }
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
    500,
    false
    )
    controller.moveSprite(mySprite)
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
    statusbar.attachToSprite(mySprite2, 5, 0)
    mySprite2.x = 160
    mySprite2.y = randint(20, 100)
    mySprite2.setVelocity(randint(speed / 2, speed), randint(-2, 2))
    mySprite2.setFlag(SpriteFlag.AutoDestroy, true)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.powerup, function (sprite, otherSprite) {
    otherSprite.destroy(effects.smiles, 200)
    music.jumpUp.play()
    powerlevel += 1
    if (powerlevel == 3) {
        shieldup()
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy(effects.fire, 200)
    statusbars.getStatusBarAttachedTo(StatusBarKind.Health, otherSprite).value += randint(-99, -101)
    if (statusbars.getStatusBarAttachedTo(StatusBarKind.Health, otherSprite).value <= 0) {
        statusbars.getStatusBarAttachedTo(StatusBarKind.Health, otherSprite).spriteAttachedTo().destroy(effects.fire, 200)
        music.jumpDown.play()
        info.changeScoreBy(10)
        if (info.score() % 100 == 0) {
            info.changeLifeBy(1)
            speed += -10
        }
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    if (shielded > 0) {
        otherSprite.destroy(effects.fire, 200)
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
        sprite.destroy(effects.fire, 200)
        info.changeLifeBy(-1)
        otherSprite.destroy(effects.fire, 200)
        music.wawawawaa.play()
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
    }
})
let mySprite4: Sprite = null
let mySprite3: Sprite = null
let statusbar: StatusBarSprite = null
let mySprite2: Sprite = null
let mySprite: Sprite = null
let projectile2: Sprite = null
let textSprite: TextSprite = null
let speed = 0
let shielded = 0
let powerlevel = 0
let chests = 0
effects.starField.startScreenEffect()
scene.setBackgroundColor(15)
info.setLife(3)
chests = 0
let spawn_rate = 1000
powerlevel = 0
shielded = 0
music.playMelody("G B A B C5 B A B ", 246)
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
createPlayer()
game.onUpdateInterval(spawn_rate, function () {
    if (game.runtime() > 60000) {
        makeShark()
    }
    if (game.runtime() > 120000) {
        makeShark()
    }
    makeShark()
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
    } else if (powerlevel <= 2 && Math.percentChance(12)) {
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
        mySprite4.x = 160
        mySprite4.y = randint(20, 100)
        mySprite4.setVelocity(-50, 0)
        mySprite4.setFlag(SpriteFlag.AutoDestroy, false)
    }
})
