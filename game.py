import math
import random

import pygame
from pygame import mixer
import datetime


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load('games.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('spaceship.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerX = 580
playerY = 650
playerX_change = 0
playerY_change = 0

enemyImg = pygame.image.load('alien.png')
enemyImg = pygame.transform.scale(enemyImg, (50, 50))
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
noofenemies = 1

bgImg = pygame.image.load('background.jpg')
bgx = 0
bgy = 0

bulletImg = pygame.image.load('ammunition.png')
bulletImg = pygame.transform.scale(bulletImg, (50, 50))
bulletX = 0
bulletY = 760
bulletY_change = 5

ebulletImg = pygame.image.load('bullet.png')
ebulletImg = pygame.transform.scale(ebulletImg, (50, 50))
ebulletX = 0
ebulletY = 0
ebulletY_change = 2

bullet_state = "ready"
ebullet_state = "ready"

score = 0
level = 0
font = pygame.font.Font('freesansbold.ttf', 20)
textx = 10
texty = 10

def bg(x, y):
    screen.blit(bgImg, (x, y))


def scoreboard(x, y):
    global sc
    sc = font.render("Score :  " + str(level * 100 + score), True, (255, 255, 255))
    sc2 = font.render("Level  :  " + str(level), True, (255, 255, 255))
    screen.blit(sc, (x, y))
    screen.blit(sc2, (x, y + 25))
    return sc


def new_enemy():
    for i in range(noofenemies):
        enemyX.append(random.randint(0, 1160))
        enemyY.append(random.randint(10, 100))
        enemyX_change.append((random.randint(15, 25) / 100))
        enemyY_change.append(4)

def enemy(x, y, i):
    screen.blit(enemyImg, (x, y))

date = datetime.date.today()

def scores():
    from username import username1
    f = open('texting','a')
    if len(str(f)) == 0:
        pass
    else:
        f.write("\n")
    new_user=username1.rstrip()
    f.write(new_user+" "+str(level*100 + score)+" "+str(date))
    for line in f:
        for i in range(1,len(f)-1):
            if line[i] == line[i+1]:
                f.truncate()
    f.close()


def player(x, y):
    screen.blit(playerImg, (x, y))


def bullet_shoot(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x, y - 100))


def enemy_bullet(x, y):
    global ebullet_state
    ebullet_state = "fire"
    screen.blit(ebulletImg, (x, y))


def collision(enemyx, bulletx, enemyy, bullety):
    distance = math.sqrt((math.pow((enemyx - bulletx), 2)) + (math.pow((enemyy - bullety), 2)))
    if bullet_state is 'fire':
        if distance < 20:
            return True
        else:
            return False


def ecollision(playerx, ebulletx, playery, ebullety):
    distance_e = math.sqrt((math.pow((playerx - ebulletx), 2)) + (math.pow((playery - ebullety + 40), 2)))
    if ebullet_state is "fire":
        if distance_e < 27:
            return True
        else:
            return False


running = True
while running:
    once=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 3.5
            if event.key == pygame.K_UP:
                playerY_change = -3
            if event.key == pygame.K_DOWN:
                playerY_change = +3
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_m:
                mixer.music.load("background.wav")
                mixer.music.play(-1)
            if event.key == pygame.K_n:
                mixer.music.load("Silent.wav")
                mixer.music.play(-1)
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    bulletY = playerY
                    bullet_shoot(bulletX, bulletY)
                    bullet = mixer.Sound('mixkit-retro-arcade-casino-notification-211.wav')
                    bullet.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1150:
        playerX = 1150

    bg(bgx, bgy)

    new_enemy()

    for x in range(noofenemies):
        for i in range(noofenemies):
            if enemyX[x] <= playerX or enemyX[x] >= playerX:
                if ebullet_state is "ready":
                    ebulletX = enemyX[x]
                    ebulletY = enemyY[x] + 30
                    enemy_bullet(ebulletX, ebulletY)
                    ebullet_state = "fire"

    if ebullet_state is "fire":
        enemy_bullet(ebulletX, ebulletY)
        ebulletY += ebulletY_change

    if ebulletY >= 1360:
        ebullet_state = "ready"

    for i in range(noofenemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] += 1
            enemyY[i] += 6

        elif enemyX[i] >= 1150:
            enemyX_change_neg = -(enemyX_change[i])
            enemyX_change_neg += -1
            enemyX_change[i] = enemyX_change_neg
            enemyY[i] += 13

        if collision(enemyX[i], bulletX, bulletY, enemyY[i] + 32):
            bulletY = 1160
            bullet_state = "ready"
            score += 10
            enemyX[i] = (random.randint(0, 1160))
            enemyY[i] = (random.randint(10, 50))
            enemyX_change[i] = ((random.randint(1, 50)) / 100)
            Collide = mixer.Sound('mixkit-arcade-mechanical-bling-210.wav')
            Collide.play()

        enemy(enemyX[i], enemyY[i], i)

    if bullet_state is 'fire':
        bullet_shoot(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = 760
        bullet_state = 'ready'

    if score == 100:
        score = 0
        level += 1
        noofenemies += 1
        new = mixer.Sound('mixkit-positive-interface-beep-221.wav')
        new.play()

    player(playerX, playerY)

    for i in range(noofenemies):
        if enemyY[i] >= 730 or ecollision(playerX, ebulletX, ebulletY, playerY + 32):
            ebullet_state = "ready"
            screen.fill('black')
            scores()
            if enemyY[i] <= 2000:
                over = mixer.Sound('mixkit-arcade-game-explosion-1699.wav')
                over.play()
            for j in range(noofenemies):
                enemyY[j] = 3000
            break

    scoreboard(textx, texty)

    pygame.display.update()
