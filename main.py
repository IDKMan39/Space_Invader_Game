# ----------------------------------------------------------------------
import pygame
import time
import random
import math
from pygame import mixer
#initialize
pygame.init()
# ----------------------------------------------------------------------
#Flaticon.com
#Zapsplat.com - sound
# To get other fonts you have to download dafont.com place ttf into folder and write name.

# ----------------------------------------------------------------------
#Screen creation
#screen = pygame.display.set_mode((width of window,hieght of window))
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Game")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#Player
playerImg = pygame.image.load("spaceshipperson.png")
playerX = 350
playerY = 450
playerspeedX = 0

#Enemy
EnemyList = []
EnemyX = []
EnemyY = []
EnemyspeedX = []
EnemyspeedY = []
EnemyImg = []

num_of_enemies = 6
for i in range(num_of_enemies) :
    EnemyImg.append(pygame.image.load("skull.png"))
    EnemyX.append(random.randint(0,735))
    EnemyY.append(random.randint(50,150))
    EnemyspeedX.append(.3)
    EnemyspeedY.append(40)

#Bullet
BulletImg = pygame.image.load("bullet.png")
BulletX = random.randint(0,800)
BulletY = 450
BulletspeedX = 0
BulletspeedY = 2
    #Ready means hidden, fire the bullet is moving
Bullet_state = "ready"


#Score Text
scoreval = 0
font = pygame.font.Font('freesansbold.ttf',32)
textx = 10
texty = 10

#Game over text

overfont=pygame.font.Font('freesansbold.ttf',64)


# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
def game_over_text() :
    over_text = overfont.render("GAME OVER",True,(69, 181, 67))
    screen.blit(over_text,(200,250))
def show_score(x,y) :
    score = font.render("Score : " + str(scoreval),True,(199, 20, 26))
    screen.blit(score,(x,y))
def player(x,y) :
    #blit is draw
    screen.blit(playerImg,(x,y))
def enemy(x,y,i) :
    #blit is draw
    screen.blit(EnemyImg[i],(x,y))
def fire_bullet(x,y) :
    global Bullet_state
    Bullet_state = "fire"
    # a small bit above the ship
    screen.blit(BulletImg,(x + 16,y + 10))
def isCollision(EnemyX,EnemyY,BulletX,BulletY) :
    distance = math.sqrt(math.pow(EnemyX-BulletX,2) + math.pow(EnemyY-BulletY,2))

    if distance < 27 and Bullet_state == "fire"  :
        return True
    else :
        return False
# ----------------------------------------------------------------------


running = True
while running :
    screen.fill((0, 0, 0))

    #Events loop
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False


        # Keystroke and then right left
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                playerspeedX = -0.5

            elif event.key == pygame.K_RIGHT :
                playerspeedX = 0.5

            elif event.key == pygame.K_SPACE and Bullet_state == "ready":
                bullet_sound = mixer.Sound("LaserGun.wav")
                bullet_sound.play()
                BulletX = playerX
                fire_bullet(BulletX,BulletY)


        elif event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT:
                playerspeedX=0

            elif event.key == pygame.K_RIGHT :
                playerspeedX = 0


    #Player Movement
    playerX += playerspeedX

    if playerX <= 0 :
        playerX = 0
    elif playerX >= 736 :
        playerX = 736

    #Enemy Movement
    for i in range(num_of_enemies) :
        #game over
        if EnemyY[i] > 350 :
            for j in range(num_of_enemies) :
                EnemyY[j] = 2000
                game_over_text()

        # Reg
        EnemyX[i] += EnemyspeedX[i]
        if EnemyX[i] <= 0 :
            EnemyspeedX[i] = .4
            EnemyY[i] += EnemyspeedY[i]
        elif EnemyX[i] >= 736 :
            EnemyspeedX[i] = -.4
            EnemyY[i] += EnemyspeedY[i]
        #Collision
        if isCollision(EnemyX[i],EnemyY[i],BulletX,BulletY) :
            bullet_sound = mixer.Sound("explosion_small.wav")
            bullet_sound.play()
            BulletY = 450
            Bullet_state = "ready"
            EnemyX[i] = random.randint(0,735)
            EnemyY[i] = random.randint(50,150)

            scoreval += 1


        enemy(EnemyX[i],EnemyY[i],i)

    # Bullet Movement
    if BulletY <= 0 :
        BulletY = 450
        Bullet_state = "ready"
    if Bullet_state == "fire" :
        fire_bullet(BulletX,BulletY)
        BulletY -= BulletspeedY





    player(playerX,playerY)
    show_score(textx,texty)
    #update
    pygame.display.update()
# ----------------------------------------------------------------------
