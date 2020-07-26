import pygame,sys,time,random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
window = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)

pygame.display.set_caption("Sprites and Sound")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

player = pygame.Rect(300,100,40,40)
playerImage = pygame.image.load('player.jpg')
playerStretchImage = pygame.transform.scale(playerImage,(40,40))
foodImage = pygame.image.load("food.png")
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-20), random.randint(0,WINDOWHEIGHT-20), 2, 2))

foodCounter = 0
NEWFOOD = 10

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == ord('w'):
                moveUp = True
                moveDown = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = True
                moveRight = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = True
                moveLeft = False

        if event.type == KEYUP:
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False


    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))
    window.fill(BLACK)

    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    window.blit(playerStretchImage,player)

    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left,player.top,player.width+2,player.height+2)
            playerStretchImage = pygame.transform.scale(playerImage,(player.width,player.height))


        for food in foods:
            window.blit(foodImage,food)
        pygame.display.update()
        mainClock.tick(40)


