# all imports
import pygame
import sys
import random, time
from pygame.locals import *

pygame.init() #initializing 

pygame.mixer.music.load('mus.wav')
pygame.mixer.music.play(-1)

fps = pygame.time.Clock()
FPS = 80

#colors
black = pygame.Color(0, 0, 0) 
white = pygame.Color(255, 255, 255)
grey = pygame.Color(128, 128, 128)
red = pygame.Color(255, 0, 0)

# variables 
screen_width = 400
screen_height = 600 
speed = 5
score = 0
COIN_SCORE = 0
TOTAL = 0
last_milestone = 0

# fonts
font = pygame.font.SysFont("Verdana", 60)
font_middle = pygame.font.SysFont("Verdana", 40)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game over", True, black)
coin_s = font_middle.render("Your score: ", True, black)

background = pygame.image.load("road.png")

#creating screen with white background
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(white)
pygame.display.set_caption("Racer")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.PNG")
        self.image = pygame.transform.scale_by(self.image, 0.15)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width-40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), 0)

# player's class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("user.PNG")
        self.image = pygame.transform.scale_by(self.image, 0.2)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) #where it will start
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]: #moving left
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width:
            if pressed_keys[K_RIGHT]: #moving the car right
                self.rect.move_ip(5, 0)

   
coin_image = pygame.image.load("coin.png")
#coin's class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image.copy()
        self.weight = random.choice([1, 3, 5])
        if self.weight == 1:
            self.image = pygame.transform.scale_by(self.image, 0.15)
        elif self.weight == 3:
            self.image = pygame.transform.scale_by(self.image, 0.2)
        else:
            self.image = pygame.transform.scale_by(self.image, 0.25)

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0) #random position above

    def move(self):
        self.rect.move_ip(0, speed) #motion downright 
        if self.rect.top > 600: #the coins go always in the screen not outside
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), 0)

    
#creating objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

#group of sprites
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


#main game cycle
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(score), True, black) #displayng scores
    coin_scores = font_small.render(str(COIN_SCORE), True, black)
    total = font_small.render(str(TOTAL), True, black)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_scores, (375, 10))
    DISPLAYSURF.blit(total, (365, 30))

    #moving sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect) 
        entity.move()
    
    #checking coin score
    for coin in coins:
        if P1.rect.colliderect(coin.rect):
            COIN_SCORE = coin.weight 
            TOTAL += coin.weight 
            coin.kill()
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
            break
    

    if TOTAL % 20 == 0 and TOTAL != 0:
        speed += 1
        TOTAL += 1

    #checking the collision with enemy cars
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(red)
        DISPLAYSURF.blit(game_over, (30, 230))
        DISPLAYSURF.blit(coin_s, (50, 310))
        coin_scores2 = font_middle.render(str(TOTAL), True, black)
        DISPLAYSURF.blit(coin_scores2, (290, 310))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    fps.tick(FPS)