import pygame
import math
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 840, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")
done = False

background = pygame.image.load("/Users/uldanakonyratbaeva/Desktop/lab 7/mickey.JPG")  
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
right_hand = pygame.image.load("/Users/uldanakonyratbaeva/Desktop/lab 7/right hand.PNG")   
right_hand = pygame.transform.scale(right_hand, (106, 331))
left_hand = pygame.image.load("/Users/uldanakonyratbaeva/Desktop/lab 7/left hand.PNG")  
left_hand = pygame.transform.scale(left_hand, (107, 243))
rect = background.get_rect(center = (420, 320))

while not done:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time = datetime.now().time()

    right_angle = -(time.second * 6)
    rotated_right_hand = pygame.transform.rotate(right_hand, right_angle)
    right_rect = rotated_right_hand.get_rect(center = rect.center)
    screen.blit(rotated_right_hand, right_rect.topleft)

    left_angle = -(time.minute * 6)
    rotated_left_hand = pygame.transform.rotate(left_hand, left_angle)
    left_rect = rotated_left_hand.get_rect(center = rect.center)
    screen.blit(rotated_left_hand, left_rect.topleft)

    pygame.display.flip()
