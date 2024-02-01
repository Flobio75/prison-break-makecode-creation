@namespace
class SpriteKind:
    Background = SpriteKind.create()
def level8():
    global bomberSpeed, bombCount, bombScore, bombsDropped, directionChangeLB, directionChangeUB, directionChange, dropIntervalLB, dropIntervalUB, dropInterval, dropSpeed, successState
    bomberSpeed = 100
    bombCount = 150
    bombScore = 8
    bombsDropped = 0
    directionChangeLB = 500
    directionChangeUB = 1500
    directionChange = randint(directionChangeLB, directionChangeUB)
    dropIntervalLB = 100
    dropIntervalUB = 150
    dropInterval = randint(dropIntervalLB, dropIntervalUB)
    dropSpeed = 100
    successState = 0
def level4():
    global bomberSpeed, bombCount, bombScore, bombsDropped, directionChangeLB, directionChangeUB, directionChange, dropIntervalLB, dropIntervalUB, dropInterval, dropSpeed, successState
    bomberSpeed = 50
    bombCount = 40
    bombScore = 4
    bombsDropped = 0
    directionChangeLB = 1000
    directionChangeUB = 2500
    directionChange = randint(directionChangeLB, directionChangeUB)
    dropIntervalLB = 300
    dropIntervalUB = 500
    dropInterval = randint(dropIntervalLB, dropIntervalUB)
    dropSpeed = 40
    successState = 1
def checkExplosion():
    for value in sprites.all_of_kind(SpriteKind.projectile):
        if value.y > scene.screen_height():
            levelFail()
def level1():
    global bomberSpeed, bombCount, bombScore, bombsDropped, directionChangeLB, directionChangeUB, directionChange, dropIntervalLB, dropIntervalUB, dropInterval, dropSpeed, successState
    bomberSpeed = 20
    bombCount = 10
    bombScore = 1
    bombsDropped = 0
    directionChangeLB = 2500
    directionChangeUB = 5000
    directionChange = randint(directionChangeLB, directionChangeUB)
    dropIntervalLB = 900
    dropIntervalUB = 1100
    dropInterval = randint(dropIntervalLB, dropIntervalUB)
    dropSpeed = 10
    successState = 1
def initBaddy():
    global baddyImages, baddy
    baddyImages = [assets.image("""
            sadEscaper
        """),
        assets.image("""
            happyEscapy
        """)]
    baddy = sprites.create(baddyImages[0], SpriteKind.enemy)
    baddy.set_position(10, 15)
    baddy.set_stay_in_screen(True)

def on_a_pressed():
    startLevel(currentLevel2)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def syncBuckets():
    index = 0
    while index <= len(buckets) - 2:
        buckets[index + 1].x = buckets[0].x
        index += 1
    bomb.x = baddy.x
def level6():
    global bomberSpeed, bombCount, bombScore, bombsDropped, directionChangeLB, directionChangeUB, directionChange, dropIntervalLB, dropIntervalUB, dropInterval, dropSpeed, successState
    bomberSpeed = 70
    bombCount = 75
    bombScore = 6
    bombsDropped = 0
    directionChangeLB = 900
    directionChangeUB = 1900
    directionChange = randint(directionChangeLB, directionChangeUB)
    dropIntervalLB = 100
    dropIntervalUB = 200
    dropInterval = randint(dropIntervalLB, dropIntervalUB)
    dropSpeed = 60
    successState = 1
def level5():
    global bomberSpeed, bombCount, bombScore, bombsDropped, directionChangeLB, directionChangeUB, directionChange, dropIntervalLB, dropIntervalUB, dropInterval, dropSpeed, successState
    bomberSpeed = 60
    bombCount = 50
    bombScore = 5
    bombsDropped = 0
    directionChangeLB = 1000
    directionChangeUB = 2000
    directionChange = randint(directionChangeLB, directionChangeUB)
    dropIntervalLB = 100
    dropIntervalUB = 300
    dropInterval = randint(dropIntervalLB, dropIntervalUB)
    dropSpeed = 50
    successState = 1
def level3():
    global bomberSpeed, bombCount, bombScore, bombsDropped, directionChangeLB, directionChangeUB, directionChange, dropIntervalLB, dropIntervalUB, dropInterval, dropSpeed, successState
    bomberSpeed = 40
    bombCount = 30
    bombScore = 3
    bombsDropped = 0
    directionChangeLB = 1500
    directionChangeUB = 3000
    directionChange = randint(directionChangeLB, directionChangeUB)
    dropIntervalLB = 500
    dropIntervalUB = 700
    dropInterval = randint(dropIntervalLB, dropIntervalUB)
    dropSpeed = 30
    successState = 1
def level2():
    global bomberSpeed, bombCount, bombScore, bombsDropped, directionChangeLB, directionChangeUB, directionChange, dropIntervalLB, dropIntervalUB, dropInterval, dropSpeed, successState
    bomberSpeed = 30
    bombCount = 20
    bombScore = 2
    bombsDropped = 0
    directionChangeLB = 1500
    directionChangeUB = 4000
    directionChange = randint(directionChangeLB, directionChangeUB)
    dropIntervalLB = 700
    dropIntervalUB = 900
    dropInterval = randint(dropIntervalLB, dropIntervalUB)
    dropSpeed = 20
    successState = 1

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(bombScore)
    sprites.destroy(otherSprite, effects.fountain, 500)
    music.play(music.create_sound_effect(WaveShape.NOISE,
            400000,
            450000,
            255,
            0,
            250,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def pauseLevel():
    global gameState, baddyFace
    gameState = 2
    controller.move_sprite(playerSprite, 0, 0)
    playerSprite.set_velocity(0, 0)
    baddy.set_velocity(0, 0)
    for value2 in sprites.all_of_kind(SpriteKind.projectile):
        value2.vy = 0
    baddy.say_text("hahaha")
    baddyFace = 1
    baddy.set_image(baddyImages[baddyFace])
def initPlayfield():
    global directionChange, buckets, row, value4, bomb, playerSprite, bucket
    directionChange = 0
    buckets = []
    scene.set_background_color(9)
    row = 30
    for index2 in range(161):
        value4 = sprites.create(assets.image("""
            TopRow
        """), SpriteKind.Background)
        value4.set_position(index2, row)
        index2 += 15
    row = 37
    for index3 in range(15):
        for column in range(161):
            value4 = sprites.create(assets.image("""
                brickWall
            """), SpriteKind.Background)
            value4.set_position(column, row)
            column += 13
        row += 6
    initBaddy()
    bomb = sprites.create(assets.image("""
        babomb
    """), SpriteKind.projectile)
    bomb.set_stay_in_screen(True)
    bomb.set_position(baddy.x, 25)
    animation.run_image_animation(bomb, assets.animation("""
        litbomb
    """), 200, True)
    playerSprite = sprites.create(assets.image("""
        bucket
    """), SpriteKind.player)
    playerSprite.set_position(scene.screen_width() / 2, scene.screen_height() - 36)
    playerSprite.set_stay_in_screen(True)
    buckets.append(playerSprite)
    for index4 in range(2):
        bucket = sprites.create(assets.image("""
            bucket
        """), SpriteKind.player)
        bucket.set_position(scene.screen_width() / 2,
            playerSprite.y + (12 + index4 * 12))
        buckets.append(bucket)
def level7():
    global bomberSpeed, bombCount, bombScore, bombsDropped, directionChangeLB, directionChangeUB, directionChange, dropIntervalLB, dropIntervalUB, dropInterval, dropSpeed, successState
    bomberSpeed = 90
    bombCount = 100
    bombScore = 7
    bombsDropped = 0
    directionChangeLB = 800
    directionChangeUB = 1800
    directionChange = randint(directionChangeLB, directionChangeUB)
    dropIntervalLB = 100
    dropIntervalUB = 200
    dropInterval = randint(dropIntervalLB, dropIntervalUB)
    dropSpeed = 80
    successState = 1
def updateGame():
    global gameState
    syncBuckets()
    checkExplosion()
    if gameState == 0:
        if bombsDropped < bombCount:
            
            def on_throttle():
                global bomb, dropInterval, bombsDropped
                bomb.set_velocity(0, dropSpeed)
                bomb = sprites.create(assets.image("""
                    babomb
                """), SpriteKind.projectile)
                bomb.set_position(baddy.x, 25)
                animation.run_image_animation(bomb, assets.animation("""
                    litbomb
                """), 200, True)
                dropInterval = randint(dropIntervalLB, dropIntervalUB)
                bombsDropped += 1
                
                def on_background():
                    global bomberSpeed
                    if baddy.x <= 8:
                        bomberSpeed = bomberSpeed * -1
                        baddy.set_velocity(bomberSpeed, 0)
                    elif baddy.x >= 148:
                        bomberSpeed = bomberSpeed * -1
                        baddy.set_velocity(bomberSpeed, 0)
                    else:
                        
                        def on_throttle2():
                            global bomberSpeed, directionChange
                            bomberSpeed = bomberSpeed * -1
                            baddy.set_velocity(bomberSpeed, 0)
                            directionChange = randint(directionChangeLB, directionChangeUB)
                        timer.throttle("changeDirection", directionChange, on_throttle2)
                        
                timer.background(on_background)
                
            timer.throttle("BombDrop", dropInterval, on_throttle)
            
        else:
            gameState = 2
    elif gameState == 2:
        baddy.set_velocity(0, 0)
        if len(sprites.all_of_kind(SpriteKind.projectile)) == 1:
            updateLevel()
        else:
            checkExplosion()
def updateLevel():
    global currentLevel2, gameState
    currentLevel2 += successState
    gameState = 1
def startLevel(currentLevel: number):
    global gameState, baddyFace
    if currentLevel == 1:
        level1()
    elif currentLevel == 2:
        level2()
    elif currentLevel == 3:
        level3()
    elif currentLevel == 4:
        level4()
    elif currentLevel == 5:
        level5()
    elif currentLevel == 6:
        level6()
    elif currentLevel == 7:
        level7()
    else:
        level8()
    gameState = 0
    controller.move_sprite(playerSprite, 100, 0)
    playerSprite.set_velocity(100, 0)
    baddy.set_velocity(bomberSpeed, 0)
    if baddyFace == 1:
        baddyFace = 0
        baddy.set_image(baddyImages[baddyFace])
def levelFail():
    global successState
    pauseLevel()
    for value3 in sprites.all_of_kind(SpriteKind.projectile):
        sprites.destroy(sprites.all_of_kind(SpriteKind.projectile).pop(),
            effects.fire,
            500)
        music.play(music.melody_playable(music.buzzer),
            music.PlaybackMode.UNTIL_DONE)
    sprites.destroy(buckets.pop())
    if currentLevel2 == 1:
        successState = 0
    else:
        successState = -1
    updateLevel()
bucket: Sprite = None
value4: Sprite = None
row = 0
baddyFace = 0
playerSprite: Sprite = None
bomb: Sprite = None
buckets: List[Sprite] = []
baddy: Sprite = None
baddyImages: List[Image] = []
successState = 0
dropSpeed = 0
dropInterval = 0
dropIntervalUB = 0
dropIntervalLB = 0
directionChange = 0
directionChangeUB = 0
directionChangeLB = 0
bombsDropped = 0
bombScore = 0
bombCount = 0
bomberSpeed = 0
gameState = 0
currentLevel2 = 0
initPlayfield()
currentLevel2 = 1
gameState = 1

def on_on_update():
    updateGame()
game.on_update(on_on_update)
