import pygame
import random
import time

# initializing
pygame.init()

# colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# fonts
font = pygame.font.SysFont("Verdana", 60)
font_middle = pygame.font.SysFont("Verdana", 40)
font_small = pygame.font.SysFont("Verdana", 20)

# variables
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20  # snake step size

# setting screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# snake and food
snake = [(100, 100), (80, 100), (60, 100)]  # starting position
snake_dir = (CELL_SIZE, 0)  # initial direction
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))  # first food
score = 0  
level = 1 
speed = 10  # initial speed

# making sure the food won't appear on the snake
def generate_food():
    while True:
        new_food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        if new_food not in snake:
            return new_food

# main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE): 
                snake_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE): 
                snake_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0): 
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0): 
                snake_dir = (CELL_SIZE, 0)

    # move snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # game over conditions
    if (new_head[0] < 0 or new_head[0] >= WIDTH or 
        new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake):
        try:
            pygame.mixer.Sound('gameover.mp3').play()
        except pygame.error:
            print("Sound file missing")
        time.sleep(0.5)
        
        screen.fill(RED)
        game_over_text = font.render("Game Over", True, BLACK)
        screen.blit(game_over_text, (150, 120))
        
        score_text = font_middle.render(f"Your score: {score}", True, BLACK)
        screen.blit(score_text, (170, 220))
        
        level_text = font_middle.render(f"Your level: {level}", True, BLACK)
        screen.blit(level_text, (180, 270))

        pygame.display.flip()
        time.sleep(3)
        break  
    
    snake.insert(0, new_head)  

    # food eaten
    if new_head == food:
        score += 1
        food = generate_food()
        try:
            pygame.mixer.Sound('success.mp3').play()
        except pygame.error:
            print("Sound file missing")

        if score % 4 == 0:
            level += 1
            speed += 2  
    else:
        snake.pop()  
    
    # draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    # draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    
    # display score and level
    score_text = font_small.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
