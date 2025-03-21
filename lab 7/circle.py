import pygame

pygame.init()
screen = pygame.display.set_mode((800, 700))
done = False

x = 400
y = 350

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        if y<=30:
            y = y
        else:
            y -= 20
    if pressed[pygame.K_DOWN]: 
        if y>=670:
            y = y
        else:
            y +=20
    if pressed[pygame.K_LEFT]: 
        if x<=25:
            x = x
        else:
            x -= 20
    if pressed[pygame.K_RIGHT]:
        if x>=775:
            x = x
        else:
            x += 20

    screen.fill((255, 228, 246))
    
    pygame.draw.circle(screen, (155, 0, 0), (x, y), 25)


    pygame.display.flip()
    clock.tick(10)