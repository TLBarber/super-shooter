@namespace
class SpriteKind:
    powerup = SpriteKind.create()
    autofire_power = SpriteKind.create()
def normalfire():
    global projectile2, powerup_counter, powerlevel
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
            if powerup_counter == 250:
                powerup_counter += -250
                powerlevel += -1

def on_b_pressed():
    music.jump_up.play()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap(sprite, otherSprite):
    global autofire, autofire_indicator
    otherSprite.destroy(effects.smiles, 200)
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
    autofire_indicator.set_position(49, 8)
sprites.on_overlap(SpriteKind.player, SpriteKind.autofire_power, on_on_overlap)

def on_a_pressed():
    normalfire()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def shieldup():
    global shielded
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

def on_a_repeated():
    global rapidfirelaser, projectile_count, autofire, delaycounter
    if autofire == 1:
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
            autofire_indicator.destroy()
    else:
        if firedelay == delaycounter:
            normalfire()
            delaycounter = 0
        else:
            delaycounter += 1
controller.A.on_event(ControllerButtonEvent.REPEATED, on_a_repeated)

def on_on_overlap2(sprite, otherSprite):
    global chests
    otherSprite.destroy(effects.hearts, 200)
    music.ba_ding.play()
    chests += 1
    textSprite.set_text("x" + convert_to_text(chests))
    if chests == 10:
        game.over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

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
    statusbar = statusbars.create(20, 4, StatusBarKind.health)
    statusbar.attach_to_sprite(mySprite2, 5, 0)
    mySprite2.x = 160
    mySprite2.y = randint(20, 100)
    mySprite2.set_velocity(randint(speed / 2, speed), randint(-2, 2))
    mySprite2.set_flag(SpriteFlag.AUTO_DESTROY, True)

def on_on_overlap3(sprite, otherSprite):
    global powerlevel, powerup_counter
    otherSprite.destroy(effects.smiles, 200)
    music.jump_up.play()
    powerlevel += 1
    if powerlevel == 3:
        shieldup()
        powerlevel += -1
    else:
        powerup_counter = 0
sprites.on_overlap(SpriteKind.player, SpriteKind.powerup, on_on_overlap3)

def on_on_overlap4(sprite, otherSprite):
    global speed
    sprite.destroy(effects.fire, 200)
    statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite).value += randint(-99, -101)
    if statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite).value <= 0:
        statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite).sprite_attached_to().destroy(effects.fire, 200)
        music.jump_down.play()
        info.change_score_by(10)
        if info.score() % 100 == 0:
            speed += -20
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap4)

def on_on_overlap5(sprite, otherSprite):
    global shielded, powerlevel, mySprite
    if shielded > 0:
        otherSprite.destroy(effects.fire, 200)
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
        sprite.destroy(effects.fire, 200)
        info.change_life_by(-1)
        otherSprite.destroy(effects.fire, 200)
        music.wawawawaa.play()
        if 0 < powerlevel:
            powerlevel += -1
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
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap5)

autofire_sprite: Sprite = None
mySprite4: Sprite = None
mySprite3: Sprite = None
statusbar: StatusBarSprite = None
mySprite2: Sprite = None
rapidfirelaser: Sprite = None
autofire_indicator: TextSprite = None
mySprite: Sprite = None
projectile2: Sprite = None
powerup_counter = 0
delaycounter = 0
firedelay = 0
projectile_count = 0
autofire = 0
textSprite: TextSprite = None
speed = 0
shielded = 0
powerlevel = 0
chests = 0
setup_complete = 0
setup_complete = 0
effects.star_field.start_screen_effect()
scene.set_background_color(15)
info.set_life(3)
chests = 0
spawn_rate = 1000
powerlevel = 0
shielded = 0
speed = -20
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
createPlayer()
autofire = 0
projectile_count = 0
firedelay = 10
delaycounter = 0
powerup_counter = 0
setup_complete = 1

def on_update_interval():
    global mySprite3, mySprite4, autofire_sprite
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
        mySprite3.set_flag(SpriteFlag.AUTO_DESTROY, False)
        makeShark()
        makeShark()
    elif powerlevel <= 2 and shielded == 0 and Math.percent_chance(12):
        if powerlevel == 2:
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
                SpriteKind.powerup)
            animation.run_image_animation(mySprite4,
                [img("""
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
                    """),
                    img("""
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
                    """),
                    img("""
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
                    """)],
                500,
                False)
        else:
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
        mySprite4.set_flag(SpriteFlag.AUTO_DESTROY, False)
    if Math.percent_chance(1):
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
game.on_update_interval(spawn_rate, on_update_interval)
