import pygame
import random
import time

# Constants
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PURPLE = (159, 0, 255)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
INITIAL_SPEED = 10
FOOD_LIFETIME = 7000  # 7 seconds
POINTS_PER_LEVEL = 4

# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_middle = pygame.font.SysFont("Verdana", 40)
font_small = pygame.font.SysFont("Verdana", 20)

# Food types
FOOD_TYPES = [
    {"points": 1, "color": RED},
    {"points": 3, "color": PURPLE},
    {"points": 5, "color": BLUE}
]

def generate_food(snake):
    """Generate food at a random position not occupied by the snake."""
    possible_positions = [
        (x, y)
        for x in range(0, WIDTH, CELL_SIZE)
        for y in range(0, HEIGHT, CELL_SIZE)
        if (x, y) not in snake
    ]
    if not possible_positions:
        return None  # Snake fills the screen
    pos = random.choice(possible_positions)
    food_type = random.choice(FOOD_TYPES)
    return {
        "pos": pos,
        "points": food_type["points"],
        "color": food_type["color"],
        "spawn_time": pygame.time.get_ticks()
    }

def show_game_over(score, level):
    """Display game over screen."""
    screen.fill(RED)
    pygame.mixer.Sound('gameover.mp3').play()

    game_over_text = font.render("Game Over", True, BLACK)
    screen.blit(game_over_text, (150, 120))
    
    score_text = font_middle.render(f"Your score: {score}", True, BLACK)
    screen.blit(score_text, (170, 220))
    
    level_text = font_middle.render(f"Your level: {level}", True, BLACK)
    screen.blit(level_text, (180, 270))
    
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()


snake = [(100, 100), (80, 100), (60, 100)]
snake_dir = (CELL_SIZE, 0)
food = generate_food(snake)
score = 0
level = 1
speed = INITIAL_SPEED
last_level_up_score = 0
running = True
game_active = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_active:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)

    if not game_active:
        continue

        # Move snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

        # Check game over
    if (new_head in snake or
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        game_active = False
        show_game_over(score, level)
        continue


    snake.insert(0, new_head)

    # Check food expiration
    current_time = pygame.time.get_ticks()
    if current_time - food["spawn_time"] > FOOD_LIFETIME:
        food = generate_food(snake)

    # Check if food eaten
    if new_head == food["pos"]:
        pygame.mixer.Sound('success.mp3').play()
        score += food["points"]
        if score - last_level_up_score >= POINTS_PER_LEVEL:
            level += 1
            speed += 1
            last_level_up_score = score
        food = generate_food(snake)
    else:
        snake.pop()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, food["color"], (*food["pos"], CELL_SIZE, CELL_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
        
    score_text = font_small.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
        
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
