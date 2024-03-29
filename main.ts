namespace SpriteKind {
    export const Background = SpriteKind.create()
}
function level8 () {
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
}
function level4 () {
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
}
function checkExplosion () {
    for (let value of sprites.allOfKind(SpriteKind.Projectile)) {
        if (value.y > scene.screenHeight()) {
            baddy.setImage(baddyImages[currentLevel + 8])
            levelFail()
        }
    }
}
function level1 () {
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
}
function addBucket (numBuckets: number) {
    bucket = sprites.create(assets.image`bucket`, SpriteKind.Player)
    bucket.setPosition(scene.screenWidth() / 2, playerSprite.y + (12 + numBuckets * 12))
    buckets.push(bucket)
}
function initBaddy () {
    baddyImages = [
    assets.image`happyEscaper04`,
    assets.image`sadEscaper1`,
    assets.image`sadEscaper2`,
    assets.image`sadEscaper3`,
    assets.image`sadEscaper4`,
    assets.image`sadEscaper5`,
    assets.image`sadEscaper6`,
    assets.image`sadEscaper7`,
    assets.image`sadEscaper8`,
    assets.image`happyEscaper04`,
    assets.image`happyEscaper04`,
    assets.image`happyEscaper04`,
    assets.image`happyEscaper4`,
    assets.image`happyEscaper5`,
    assets.image`happyEscaper6`,
    assets.image`happyEscaper7`,
    assets.image`happyEscaper8`,
    assets.image`surpriseEscaper13`,
    assets.image`surpriseEscaper13`,
    assets.image`surpriseEscaper13`,
    assets.image`surpriseEscaper4`,
    assets.image`surpriseEscaper5`,
    assets.image`surpriseEscaper6`,
    assets.image`surpriseEscaper7`,
    assets.image`surpriseEscaper8`
    ]
    baddy = sprites.create(baddyImages[0], SpriteKind.Enemy)
    baddy.setPosition(10, 15)
    baddy.setStayInScreen(true)
    baddy.setBounceOnWall(true)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    startLevel(currentLevel)
})
function syncBuckets () {
    for (let index = 0; index <= buckets.length - 2; index++) {
        buckets[index + 1].x = buckets[0].x
    }
    bomb.x = baddy.x
}
function level6 () {
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
}
function level5 () {
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
}
function level3 () {
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
}
function level2 () {
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
}
function checkBuckets () {
    if (buckets.length == 0) {
        game.gameOver(false)
        game.setGameOverEffect(false, effects.confetti)
    }
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
    initBaddy()
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
    console.logValue("x", MAX_BUCKETS - 2)
    for (let index = 0; index <= MAX_BUCKETS - 2; index++) {
        console.logValue("x", MAX_BUCKETS - 2)
        addBucket(index)
        console.logValue("buckets=", buckets.length)
    }
}
function extraLife () {
    if (info.score() >= nextExtraLife) {
        music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
        nextExtraLife += MAX_LIFE_INTERVAL
        baddy.setImage(baddyImages[currentLevel + 17])
        if (buckets.length < MAX_BUCKETS) {
            addBucket(buckets.length - 1)
        }
    }
}
function level7 () {
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
}
function updateGame () {
    syncBuckets()
    checkExplosion()
    extraLife()
    checkBuckets()
    if (gameState == 0) {
        if (bombsDropped < bombCount) {
            timer.throttle("BombDrop", dropInterval, function () {
                dropBomb()
                timer.background(function () {
                    timer.throttle("changeDirection", directionChange, function () {
                        changeBaddyDirection()
                        directionChange = randint(directionChangeLB, directionChangeUB)
                    })
                })
            })
        } else {
            gameState = 2
        }
    } else if (gameState == 2) {
        baddy.setVelocity(0, 0)
        if (sprites.allOfKind(SpriteKind.Projectile).length == 1) {
            updateLevel()
        }
    }
}
function updateLevel () {
    currentLevel += successState
    gameState = 1
}
function changeBaddyDirection () {
    bomberSpeed = bomberSpeed * -1
    baddy.setVelocity(bomberSpeed, 0)
}
function startLevel (currentLevel: number) {
    if (currentLevel == 1) {
        level1()
    } else if (currentLevel == 2) {
        level2()
    } else if (currentLevel == 3) {
        level3()
    } else if (currentLevel == 4) {
        level4()
    } else if (currentLevel == 5) {
        level5()
    } else if (currentLevel == 6) {
        level6()
    } else if (currentLevel == 7) {
        level7()
    } else {
        level8()
    }
    gameState = 0
    controller.moveSprite(playerSprite, 100, 0)
    baddy.setVelocity(bomberSpeed, 0)
    baddy.setImage(baddyImages[currentLevel])
}
function levelFail () {
    pauseLevel()
    for (let value of sprites.allOfKind(SpriteKind.Projectile)) {
        sprites.destroy(sprites.allOfKind(SpriteKind.Projectile).pop(), effects.fire, 500)
        music.play(music.melodyPlayable(music.buzzer), music.PlaybackMode.UntilDone)
    }
    sprites.destroy(buckets.pop())
    if (currentLevel == 1) {
        successState = 0
    } else {
        successState = -1
    }
    updateLevel()
}
function dropBomb () {
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
}
let value: Sprite = null
let row = 0
let bomb: Sprite = null
let buckets: Sprite[] = []
let playerSprite: Sprite = null
let bucket: Sprite = null
let baddyImages: Image[] = []
let baddy: Sprite = null
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
let MAX_BUCKETS = 0
let nextExtraLife = 0
let MAX_LIFE_INTERVAL = 0
let gameState = 0
let currentLevel = 0
currentLevel = 1
gameState = 1
MAX_LIFE_INTERVAL = 1000
nextExtraLife = MAX_LIFE_INTERVAL
MAX_BUCKETS = 3
initPlayfield()
game.onUpdate(function () {
    updateGame()
})
