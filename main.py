namespace SpriteKind {
    export const Background = SpriteKind.create()
}
function checkExplosion () {
    for (let value of sprites.allOfKind(SpriteKind.Projectile)) {
        if (value.y > scene.screenHeight()) {
            levelFail()
        }
    }
}
function level1 () {
    bomberSpeed = 25
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
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    startLevel(currentLevel)
})
function syncBuckets () {
    for (let index = 0; index <= buckets.length - 2; index++) {
        console.logValue("sync index", index)
        buckets[index + 1].x = buckets.removeAt(0)
    }
    bomb.x = baddy.x
}
function level3 () {
    bomberSpeed = 100
    bombCount = 30
    bombScore = 3
    bombsDropped = 0
    directionChangeLB = 1500
    directionChangeUB = 3000
    directionChange = randint(directionChangeLB, directionChangeUB)
    dropIntervalLB = 500
    dropIntervalUB = 700
    dropInterval = randint(dropIntervalLB, dropIntervalUB)
    dropSpeed = 40
    successState = 1
}
function level2 () {
    bomberSpeed = 50
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
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    info.changeScoreBy(bombScore)
    sprites.destroy(otherSprite, effects.fountain, 500)
    music.play(music.createSoundEffect(WaveShape.Noise, 400000, 450000, 255, 0, 250, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
})
function pauseLevel () {
    gameState = 2
    controller.moveSprite(playerSprite, 0, 0)
    baddy.setVelocity(0, 0)
    for (let value of sprites.allOfKind(SpriteKind.Projectile)) {
        value.vy = 0
    }
}
function initPlayfield () {
    directionChange = 0
    buckets = []
    scene.setBackgroundColor(9)
    row = 30
    for (let index = 0; index <= 160; index++) {
        value = sprites.create(assets.image`TopRow`, SpriteKind.Background)
        value.setPosition(index, row)
        index += 15
    }
    row = 37
    for (let index = 0; index < 15; index++) {
        for (let column = 0; column <= 160; column++) {
            value = sprites.create(assets.image`brickWall`, SpriteKind.Background)
            value.setPosition(column, row)
            column += 13
        }
        row += 6
    }
    baddy = sprites.create(assets.image`sadEscaper`, SpriteKind.Enemy)
    baddy.setPosition(10, 15)
    baddy.setStayInScreen(true)
    bomb = sprites.create(assets.image`babomb`, SpriteKind.Projectile)
    bomb.setStayInScreen(true)
    bomb.setPosition(baddy.x, 25)
    animation.runImageAnimation(
    bomb,
    assets.animation`litbomb`,
    200,
    true
    )
    playerSprite = sprites.create(assets.image`bucket`, SpriteKind.Player)
    playerSprite.setPosition(scene.screenWidth() / 2, scene.screenHeight() - 36)
    playerSprite.setStayInScreen(true)
    buckets.push(playerSprite)
    for (let index = 0; index <= 1; index++) {
        bucket = sprites.create(assets.image`bucket`, SpriteKind.Player)
        bucket.setPosition(scene.screenWidth() / 2, playerSprite.y + (12 + index * 12))
        buckets.push(bucket)
    }
}
function updateGame () {
    syncBuckets()
    checkExplosion()
    if (gameState == 0) {
        if (bombsDropped < bombCount) {
            checkExplosion()
            timer.throttle("BombDrop", dropInterval, function () {
                bomb.setVelocity(0, dropSpeed)
                bomb = sprites.create(assets.image`babomb`, SpriteKind.Projectile)
                bomb.setPosition(baddy.x, 25)
                animation.runImageAnimation(
                bomb,
                assets.animation`litbomb`,
                200,
                true
                )
                dropInterval = randint(dropIntervalLB, dropIntervalUB)
                bombsDropped += 1
                console.log(sprites.allOfKind(SpriteKind.Projectile).length)
                checkExplosion()
                timer.background(function () {
                    checkExplosion()
                    if (baddy.x <= 8) {
                        bomberSpeed = bomberSpeed * -1
                        baddy.setVelocity(bomberSpeed, 0)
                    } else if (baddy.x >= 148) {
                        bomberSpeed = bomberSpeed * -1
                        baddy.setVelocity(bomberSpeed, 0)
                    } else {
                        timer.throttle("changeDirection", directionChange, function () {
                            bomberSpeed = bomberSpeed * -1
                            baddy.setVelocity(bomberSpeed, 0)
                            console.log(dropInterval)
                            directionChange = randint(directionChangeLB, directionChangeUB)
                            checkExplosion()
                        })
                    }
                })
            })
            checkExplosion()
        } else {
            gameState = 2
            checkExplosion()
        }
    } else if (gameState == 2) {
        baddy.setVelocity(0, 0)
        if (sprites.allOfKind(SpriteKind.Projectile).length == 1) {
            updateLevel()
        } else {
            checkExplosion()
        }
    }
}
function updateLevel () {
    console.logValue("success state", successState)
    console.logValue("current level before", currentLevel)
    currentLevel += successState
    console.logValue("current level after", currentLevel)
    gameState = 1
}
function destroySprites () {
    if (sprites.allOfKind(SpriteKind.Projectile).length > 0) {
        music.play(music.createSoundEffect(WaveShape.Noise, 1623, 250, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    }
}
function startLevel (currentLevel: number) {
    if (currentLevel == 1) {
        level1()
    } else if (currentLevel == 2) {
        level2()
    } else if (currentLevel == 3) {
        level3()
    } else if (currentLevel == 4) {
    	
    } else if (currentLevel == 5) {
    	
    } else if (currentLevel == 6) {
    	
    } else if (currentLevel == 7) {
    	
    } else {
    	
    }
    gameState = 0
    controller.moveSprite(playerSprite, 100, 0)
    baddy.setVelocity(bomberSpeed, 0)
}
function levelFail () {
    pauseLevel()
    for (let value of sprites.allOfKind(SpriteKind.Projectile)) {
        value.setVelocity(0, 0)
        sprites.destroy(sprites.allOfKind(SpriteKind.Projectile).pop(), effects.starField, 500)
        music.play(music.melodyPlayable(music.buzzer), music.PlaybackMode.UntilDone)
    }
    if (currentLevel == 1) {
        successState = 0
    } else {
        successState = -1
    }
    updateLevel()
}
let bucket: Sprite = null
let value: Sprite = null
let row = 0
let playerSprite: Sprite = null
let baddy: Sprite = null
let bomb: Sprite = null
let buckets: Sprite[] = []
let successState = 0
let dropSpeed = 0
let dropInterval = 0
let dropIntervalUB = 0
let dropIntervalLB = 0
let directionChange = 0
let directionChangeUB = 0
let directionChangeLB = 0
let bombsDropped = 0
let bombScore = 0
let bombCount = 0
let bomberSpeed = 0
let gameState = 0
let currentLevel = 0
initPlayfield()
currentLevel = 1
gameState = 1
game.onUpdate(function () {
    updateGame()
})
