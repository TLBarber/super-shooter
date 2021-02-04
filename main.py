@namespace
class SpriteKind:
    powerup = SpriteKind.create()
    autofire_power = SpriteKind.create()
    info = SpriteKind.create()
    shield_power = SpriteKind.create()
    clearenemies = SpriteKind.create()
def normalfire():
    global projectile2, powerup_counter, powerlevel, mySprite5
    if setup_complete == 1:
        projectile2 = sprites.create_projectile_from_sprite(img("""
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
            """),
            mySprite,
            105,
            0)
        projectile2.set_flag(SpriteFlag.AUTO_DESTROY, True)
        music.pew_pew.play()
        if powerlevel >= 1:
            projectile2.y += -5
            projectile2 = sprites.create_projectile_from_sprite(img("""
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
                """),
                mySprite,
                105,
                0)
            projectile2.set_flag(SpriteFlag.AUTO_DESTROY, True)
            projectile2.y += 5
            if powerlevel == 1:
                powerup_counter += 1
                if powerup_counter == 50:
                    powerup_counter += -50
                    powerlevel += -1
                    mySprite5.destroy()
        if powerlevel >= 2:
            projectile2 = sprites.create_projectile_from_sprite(img("""
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
                """),
                mySprite,
                105,
                5)
            projectile2.y += 10
            projectile2.set_flag(SpriteFlag.AUTO_DESTROY, True)
            projectile2 = sprites.create_projectile_from_sprite(img("""
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
                """),
                mySprite,
                105,
                -5)
            projectile2.set_flag(SpriteFlag.AUTO_DESTROY, True)
            projectile2.y += -10
            powerup_counter += 1
            if powerup_counter == 50:
                quadfire.destroy()
                mySprite5 = sprites.create(img("""
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
                                            . . . . . . . . 9 9 9 . . . . . 
                                            . . . . 9 9 9 9 9 5 9 . . . . . 
                                            . . . . . . . . 9 9 9 . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . .
                    """),
                    SpriteKind.info)
                mySprite5.set_position(56, 108)
                powerup_counter += -50
                powerlevel += -1
def initialize_variables():
    global setup_complete, chests, spawn_rate, powerlevel, shielded, speed, powerup_onscreen, textSprite, autofire, projectile_count, firedelay, rapidfire, delaycounter, powerup_counter
    setup_complete = 0
    info.set_life(3)
    chests = 0
    spawn_rate = 1000
    powerlevel = 0
    shielded = 0
    speed = -20
    powerup_onscreen = 0
    textSprite = textsprite.create("x" + convert_to_text(chests), 15, 5)
    textSprite.set_icon(img("""
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
    """))
    textSprite.set_position(15, 20)
    autofire = 0
    projectile_count = 0
    firedelay = 10
    rapidfire = 0
    delaycounter = 0
    powerup_counter = 0
def holdFire():
    global delaycounter
    if firedelay == delaycounter:
        normalfire()
        delaycounter = 0
    else:
        delaycounter += 1

def on_b_pressed():
    global rapidfire
    if autofire == 1:
        rapidfire = 1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def makeEnemies():
    if game.runtime() > 60000:
        makeShark()
    if game.runtime() > 120000:
        makeShark()
        makeShark()
    if game.runtime() > 180000:
        makeShark()
        makeShark()
        makeShark()
    makeShark()

def on_on_overlap(sprite, otherSprite):
    pickupRapidFire(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.autofire_power, on_on_overlap)

def on_a_pressed():
    normalfire()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def enemyGetsShot2(projectile: Sprite, enemy: Sprite):
    statusbars.get_status_bar_attached_to(StatusBarKind.health, enemy).sprite_attached_to().destroy()

def on_on_overlap2(sprite, otherSprite):
    shieldup(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.shield_power, on_on_overlap2)

def clearScreen():
    global mySprite6
    mySprite6 = sprites.create(img("""
            ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    ........f.......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    .........f......
                    ..........f.....
        """),
        SpriteKind.clearenemies)
    mySprite6.set_velocity(500, 0)
    mySprite.set_flag(SpriteFlag.INVISIBLE, True)
    mySprite.set_flag(SpriteFlag.AUTO_DESTROY, True)
def pickupRapidFire(powerup: Sprite):
    global autofire, autofire_indicator, powerup_onscreen, projectile_count
    if autofire == 0:
        powerup.destroy(effects.smiles, 200)
        music.magic_wand.play()
        autofire += 1
        autofire_indicator = textsprite.create("x1000")
        autofire_indicator.set_icon(img("""
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
        """))
        autofire_indicator.set_position(55, 8)
        powerup_onscreen = 0
    else:
        music.magic_wand.play()
        powerup.destroy(effects.smiles, 200)
        autofire_indicator.set_text("x1000")
        projectile_count = 0
        powerup_onscreen = 0
def pickupPowerup(player2: Sprite, powerup: Sprite):
    global mySprite5, powerup_counter, powerlevel, powerup_onscreen, quadfire
    powerup.destroy(effects.smiles, 200)
    music.jump_up.play()
    if powerlevel == 0:
        mySprite5 = sprites.create(img("""
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
                            . . . . . . . . 9 9 9 . . . . . 
                            . . . . 9 9 9 9 9 5 9 . . . . . 
                            . . . . . . . . 9 9 9 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.info)
        mySprite5.set_position(56, 108)
        powerup_counter = 0
        powerlevel = 1
        powerup_onscreen = 0
    elif powerlevel == 1:
        mySprite5.destroy()
        quadfire = sprites.create(img("""
                . . . . . . . . 9 9 9 . . . . . 
                            . . . . 9 9 9 9 9 5 9 . . . . . 
                            . . . . . . . . 9 9 9 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . 9 9 9 . . . . . 
                            . . . . 9 9 9 9 9 5 9 . . . . . 
                            . . . . . . . . 9 9 9 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . 9 9 9 . . . . . 
                            . . . . 9 9 9 9 9 5 9 . . . . . 
                            . . . . . . . . 9 9 9 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . 9 9 9 . . . . . 
                            . . . . 9 9 9 9 9 5 9 . . . . . 
                            . . . . . . . . 9 9 9 . . . . .
            """),
            SpriteKind.info)
        quadfire.set_position(56, 108)
        powerup_counter = 0
        powerlevel = 2
        powerup_onscreen = 0
    else:
        mySprite5.destroy()
        powerup_counter = 0
        powerup_onscreen = 0
def enemyGetsShot(projectile: Sprite, enemy: Sprite):
    global speed
    projectile.destroy(effects.fire, 200)
    statusbars.get_status_bar_attached_to(StatusBarKind.health, enemy).value += randint(-1, -2)
    if statusbars.get_status_bar_attached_to(StatusBarKind.health, enemy).value <= 0:
        statusbars.get_status_bar_attached_to(StatusBarKind.health, enemy).sprite_attached_to().destroy(effects.fire, 200)
        music.jump_down.play()
        info.change_score_by(10)
        if info.score() % 100 == 0:
            speed += -20

def on_on_overlap3(sprite, otherSprite):
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.clearenemies,
    SpriteKind.projectile,
    on_on_overlap3)

def rapidFireButton():
    global rapidfirelaser, projectile_count, autofire, rapidfire
    rapidfirelaser = sprites.create_projectile_from_sprite(assets.image("""
        lazer
    """), mySprite, 105, 0)
    projectile2.set_flag(SpriteFlag.AUTO_DESTROY, True)
    projectile_count += 1
    music.magic_wand.play()
    autofire_indicator.set_text("x" + convert_to_text(1000 - projectile_count * 4))
    if projectile_count >= 250:
        projectile_count = 0
        autofire = 0
        rapidfire = 0
        autofire_indicator.destroy()
def shieldup(shieldsprite: Sprite):
    global shielded, powerup_onscreen
    mySprite.set_image(img("""
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
    """))
    shielded = 1
    shieldsprite.destroy(effects.rings, 100)
    powerup_onscreen = 0
def makePowerups():
    global mySprite3, mySprite4, powerup_onscreen, autofire_sprite
    if Math.percent_chance(10):
        mySprite3 = sprites.create(img("""
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
            """),
            SpriteKind.food)
        mySprite3.x = 160
        mySprite3.y = randint(20, 100)
        mySprite3.set_velocity(-30, 0)
        mySprite3.set_flag(SpriteFlag.AUTO_DESTROY, True)
        makeShark()
        makeShark()
    elif powerlevel < 2 and (powerup_onscreen == 0 and Math.percent_chance(10)):
        mySprite4 = sprites.create(img("""
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
            """),
            SpriteKind.powerup)
        mySprite4.x = 160
        mySprite4.y = randint(20, 100)
        mySprite4.set_velocity(-50, 0)
        mySprite4.set_flag(SpriteFlag.AUTO_DESTROY, True)
        powerup_onscreen = 1
    elif powerup_onscreen == 0 and Math.percent_chance(10) and shielded == 0:
        mySprite4 = sprites.create(img("""
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
            """),
            SpriteKind.shield_power)
        mySprite4.x = 160
        mySprite4.y = randint(20, 100)
        mySprite4.set_velocity(-50, 0)
        mySprite4.set_flag(SpriteFlag.AUTO_DESTROY, True)
        powerup_onscreen = 1
    if powerup_onscreen == 0 and Math.percent_chance(1):
        autofire_sprite = sprites.create(img("""
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
            """),
            SpriteKind.autofire_power)
        autofire_sprite.x = 160
        autofire_sprite.set_velocity(-50, 0)
        autofire_sprite.set_flag(SpriteFlag.AUTO_DESTROY, False)
        powerup_onscreen = 1

def on_on_overlap4(sprite, otherSprite):
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.clearenemies,
    SpriteKind.autofire_power,
    on_on_overlap4)

def pickupChest(chest: Sprite):
    global chests
    chest.destroy(effects.hearts, 200)
    music.ba_ding.play()
    chests += 1
    textSprite.set_text("x" + convert_to_text(chests))
    if chests == 10:
        game.over(True)

def on_on_overlap5(sprite, otherSprite):
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.clearenemies, SpriteKind.food, on_on_overlap5)

def on_on_overlap6(sprite, otherSprite):
    enemyGetsShot2(sprite, otherSprite)
sprites.on_overlap(SpriteKind.clearenemies, SpriteKind.enemy, on_on_overlap6)

def on_a_repeated():
    holdFire()
controller.A.on_event(ControllerButtonEvent.REPEATED, on_a_repeated)

def on_on_overlap7(sprite, otherSprite):
    pickupChest(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap7)

def on_on_overlap8(sprite, otherSprite):
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.clearenemies,
    SpriteKind.shield_power,
    on_on_overlap8)

def createPlayer():
    global mySprite
    mySprite = sprites.create(img("""
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
        """),
        SpriteKind.player)
    mySprite.x = 50
    mySprite.set_stay_in_screen(True)
    animation.run_movement_animation(mySprite,
        animation.animation_presets(animation.ease_left),
        1000,
        False)
    music.play_melody("G B A B C5 B A B ", 246)
    controller.move_sprite(mySprite)
def enemyCollision(player2: Sprite, enemy: Sprite):
    global shielded, powerlevel, mySprite5, mySprite
    if shielded > 0:
        enemy.destroy(effects.fire, 200)
        shielded = 0
        mySprite.set_image(img("""
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
        """))
    else:
        enemy.destroy(effects.fire, 200)
        info.change_life_by(-1)
        player2.destroy(effects.fire, 200)
        music.wawawawaa.play()
        clearScreen()
        if info.life() > 0:
            if 1 == powerlevel:
                powerlevel = 0
                mySprite5.destroy()
            elif 2 == powerlevel:
                powerlevel = 1
                quadfire.destroy()
                mySprite5 = sprites.create(img("""
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
                                            . . . . . . . . 9 9 9 . . . . . 
                                            . . . . 9 9 9 9 9 5 9 . . . . . 
                                            . . . . . . . . 9 9 9 . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . .
                    """),
                    SpriteKind.info)
                mySprite5.set_position(56, 108)
            if game.ask("Ready?"):
                mySprite = sprites.create(img("""
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
                    """),
                    SpriteKind.player)
                mySprite.x = 15
                mySprite.set_stay_in_screen(True)
                controller.move_sprite(mySprite)
            else:
                game.over(False, effects.melt)
        else:
            game.over(False, effects.melt)

def on_on_overlap9(sprite, otherSprite):
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.clearenemies, SpriteKind.powerup, on_on_overlap9)

def makeShark():
    global mySprite2, statusbar
    mySprite2 = sprites.create(img("""
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
        """),
        SpriteKind.enemy)
    animation.run_image_animation(mySprite2,
        [img("""
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
            """),
            img("""
                .............ccfff..............
                        ............cddbbf..............
                        ...........cddbbf...............
                        ..........fccbbcf............ccc
                        ....ffffffccccccff.........ccbbc
                        ..ffbbbbbbbbbbbbbcfff.....cdbbc.
                        ffbbbbbbbbbcbcbbbbcccff..cddbbf.
                        fbcbbbbbffbbcbcbbbcccccfffdbbf..
                        fbbb1111ff1bcbcbbbcccccccbbbcf..
                        .fb11111111bbbbbbcccccccccbccf..
                        ..fccc33cc11bbbbccccccccfffbbcf.
                        ...fc131c111bbbcccccbdbc...fbbf.
                        ....f33c111cbbbfdddddcc.....fbbf
                        .....ff1111fbdbbfddcc........fff
                        .......cccccfbdbbfc.............
                        .............fffff..............
            """),
            img("""
                ..............cfff..............
                        ............ccddbf..............
                        ...........cbddbff.........ccc..
                        ..........fccbbcf.........cbbc..
                        ...fffffffccccccff.......cdbc...
                        .ffcbbbbbbbbbbbbbcfff....cdbf...
                        fcbbbbbbbbbcbbbbbbcccff.cdbf....
                        fbcbbbbffbbbcbcbbbcccccffdcf....
                        fbb1111ffbbbcbcbbbccccccbbcf....
                        .fb11111111bbcbbbccccccccbbcf...
                        ..fccc33cb11bbbbcccccccfffbbf...
                        ...fc131c111bbbcccccbdbc..fbbf..
                        ....f33c111cbbccdddddbc....fff..
                        .....ff1111fdbbccddbcc..........
                        .......cccccfdbbbfcc............
                        .............fffff..............
            """),
            img("""
                .............ccfff..............
                        ............cddbbf..............
                        ...........cddbbf...............
                        ..........fccbbcf............ccc
                        ....ffffffccccccff.........ccbbc
                        ..ffbbbbbbbbbbbbbcfff.....cdbbc.
                        ffbbbbbbbbbcbcbbbbcccff..cddbbf.
                        fbcbbbbbffbbcbcbbbcccccfffdbbf..
                        fbbb1111ff1bcbcbbbcccccccbbbcf..
                        .fb11111111bbbbbbcccccccccbccf..
                        ..fccc33cc11bbbbccccccccfffbbcf.
                        ...fc131c111bbbcccccbdbc...fbbf.
                        ....f33c111cbbbfdddddcc.....fbbf
                        .....ff1111fbdbbfddcc........fff
                        .......cccccfbdbbfc.............
                        .............fffff..............
            """)],
        500,
        True)
    statusbar = statusbars.create(20, 4, StatusBarKind.health)
    statusbar.max = 2
    statusbar.attach_to_sprite(mySprite2, 5, 0)
    mySprite2.x = 160
    mySprite2.y = randint(20, 100)
    mySprite2.set_velocity(randint(speed / 2, speed), randint(-2, 2))
    mySprite2.set_flag(SpriteFlag.AUTO_DESTROY, True)

def on_on_overlap10(sprite, otherSprite):
    pickupPowerup(sprite, otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.powerup, on_on_overlap10)

def on_on_overlap11(sprite, otherSprite):
    enemyGetsShot(sprite, otherSprite)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap11)

def on_on_overlap12(sprite, otherSprite):
    enemyCollision(sprite, otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap12)

statusbar: StatusBarSprite = None
mySprite2: Sprite = None
autofire_sprite: Sprite = None
mySprite4: Sprite = None
mySprite3: Sprite = None
rapidfirelaser: Sprite = None
autofire_indicator: TextSprite = None
mySprite6: Sprite = None
delaycounter = 0
rapidfire = 0
firedelay = 0
projectile_count = 0
autofire = 0
textSprite: TextSprite = None
powerup_onscreen = 0
speed = 0
shielded = 0
spawn_rate = 0
chests = 0
quadfire: Sprite = None
mySprite5: Sprite = None
powerup_counter = 0
powerlevel = 0
mySprite: Sprite = None
projectile2: Sprite = None
setup_complete = 0
game.splash("Collect 10 chests", "but watch out for sharks!!")
initialize_variables()
effects.star_field.start_screen_effect()
scene.set_background_color(15)
createPlayer()
setup_complete = 1

def on_update_interval():
    makeEnemies()
    makePowerups()
game.on_update_interval(spawn_rate, on_update_interval)

def on_update_interval2():
    if rapidfire == 1:
        rapidFireButton()
game.on_update_interval(100, on_update_interval2)
