@namespace
class SpriteKind:
    powerup = SpriteKind.create()

def on_b_pressed():
    music.jump_up.play()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global projectile2
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
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def shieldup():
    global statusbar2
    statusbar2 = statusbars.create(1, 20, StatusBarKind.energy)
    statusbar2.attach_to_sprite(mySprite)
    statusbar2.max = 100
    statusbar2.value = 100
    statusbar2.set_color(9, 15)
    statusbar2.set_offset_padding(0, -20)


def on_on_overlap(sprite, otherSprite):
    global chests
    otherSprite.destroy(effects.hearts, 200)
    music.ba_ding.play()
    chests += 1
    textSprite.set_text("x" + convert_to_text(chests))
    if chests == 10:
        game.over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

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
        500,
        False)
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

def on_on_overlap2(sprite, otherSprite):
    global powerlevel
    otherSprite.destroy(effects.smiles, 200)
    music.jump_up.play()
    powerlevel += 1
    if powerlevel == 3:
        shieldup()
sprites.on_overlap(SpriteKind.player, SpriteKind.powerup, on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    global speed
    sprite.destroy(effects.halo, 100)
    statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite).value += randint(-99, -101)
    if statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite).value <= 0:
        statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite).sprite_attached_to().destroy(effects.fire, 200)
        music.jump_down.play()
        info.change_score_by(10)
        if info.score() % 100 == 0:
            info.change_life_by(1)
            speed += -10
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

def on_on_overlap4(sprite, otherSprite):
    global powerlevel, mySprite
    if statusbar2.value > 0:
        otherSprite.destroy(effects.fire, 200)
        statusbar2.value = 0
        powerlevel += -1
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
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

mySprite4: Sprite = None
mySprite3: Sprite = None
statusbar: StatusBarSprite = None
mySprite2: Sprite = None
statusbar2: StatusBarSprite = None
mySprite: Sprite = None
projectile2: Sprite = None
textSprite: TextSprite = None
powerlevel = 0
chests = 0
effects.star_field.start_screen_effect()
scene.set_background_color(15)
info.set_life(3)
chests = 0
spawn_rate = 1000
powerlevel = 0
music.play_melody("G B A B C5 B A B ", 246)
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

def on_update_interval():
    global mySprite3, mySprite4
    if game.runtime() > 60000:
        makeShark()
    if game.runtime() > 120000:
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
    else:
        if powerlevel <= 2 and Math.percent_chance(12):
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
game.on_update_interval(spawn_rate, on_update_interval)
