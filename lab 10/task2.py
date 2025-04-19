import pygame
import random
import time
import psycopg2

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

# Food types
FOOD_TYPES = [
    {"points": 1, "color": RED},
    {"points": 3, "color": PURPLE},
    {"points": 5, "color": BLUE}
]

# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_middle = pygame.font.SysFont("Verdana", 40)
font_small = pygame.font.SysFont("Verdana", 20)

class DatabaseManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="new_database",
            user="myuser",
            password="myuser",
            host="localhost",
            port="5432"
        )        
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

class UserManager:
    db: DatabaseManager
    user_id: int
    def __init__(self, username: str):
        self.db = DatabaseManager()
        self.username = username
        self.check_existance()

    def check_existance(self):
        query = "SELECT * FROM users WHERE username=%s"
        print(self.username)
        self.db.cur.execute(query, (self.username,))

        users = self.db.cur.fetchall()

        if len(users) == 0:
            self.create_user()
        else:
            self.load_user(users)

        self.get_user_id()

    def get_user_id(self):
        query = "SELECT id from users where username=%s"

        self.db.cur.execute(query, (self.username,))
        self.user_id = self.db.cur.fetchone()
        print(self.user_id)

    def create_user(self):
        query = "INSERT INTO users(username) VALUES(%s)"
        self.db.cur.execute(query, (self.username,))
        self.level = 1
        self.score = 0
        self.db.conn.commit()

    def load_user(self, users):
        user = users[0]
        query = "select * from user_score where user_id=%s"
        self.db.cur.execute(query, (user[0],))
        data = self.db.cur.fetchall()[-1]
        print(data)
        self.level = data[2]
        self.score = data[3]

    def save_userdata(self, score, level):
        query = "INSERT INTO user_score(user_id, users_level, users_score) VALUES (%s, %s, %s)"
        self.db.cur.execute(query, (self.user_id, score, level))
        self.db.conn.commit()




class Snake:
    def __init__(self, cell_size):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (cell_size, 0)
        self.cell_size = cell_size

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, head)

    def shrink(self):
        self.body.pop()

    def collided(self):
        head = self.body[0]
        return (
            head in self.body[1:] or
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT
        )

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (*segment, self.cell_size, self.cell_size))



class Food:
    def __init__(self, snake_body, cell_size):
        self.cell_size = cell_size
        self.respawn(snake_body)

    def respawn(self, snake_body):
        positions = [
            (x, y)
            for x in range(0, WIDTH, self.cell_size)
            for y in range(0, HEIGHT, self.cell_size)
            if (x, y) not in snake_body
        ]
        self.pos = random.choice(positions)
        type = random.choice(FOOD_TYPES)
        self.color = type["color"]
        self.points = type["points"]
        self.spawn_time = pygame.time.get_ticks()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (*self.pos, self.cell_size, self.cell_size))

class LevelManager:
    def __init__(self, points_per_level, initial_speed, score = 0, level = 1):
        self.score = score
        self.level = level
        self.speed = initial_speed
        self.points_per_level = points_per_level
        self.last_level_score = 0

    def add_score(self, points):
        self.score += points
        if self.score - self.last_level_score >= self.points_per_level:
            self.level += 1
            self.speed += 0.2
            self.last_level_score = self.score

    def draw(self, surface):
        text = font_small.render(f"Score: {self.score}  Level: {self.level}", True, WHITE)
        surface.blit(text, (10, 10))


username = input("Write Your username:\n")
snake = Snake(CELL_SIZE)
food = Food(snake.body, CELL_SIZE)
user = UserManager(username)
level = LevelManager(POINTS_PER_LEVEL, INITIAL_SPEED, user.score, user.level)
pause_button = pygame.Rect(WIDTH - 110, 10, 100, 40)
running = True
paused = False

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, CELL_SIZE):
                snake.direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -CELL_SIZE):
                snake.direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake.direction!= (CELL_SIZE, 0):
                snake.direction= (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-CELL_SIZE, 0):
                snake.direction = (CELL_SIZE, 0)
            elif event.key == pygame.K_SPACE:
                paused = not paused
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_button.collidepoint(event.pos):
                paused = not paused 
            
    
    if not paused:
        # Move snake
        snake.move()

        # Check game over
        if snake.collided():
            screen.fill(RED)
            game_over_text  = font.render("Game over", True, BLACK)
            screen.blit(game_over_text, (150, 120))
            score_text = font_middle.render(f"Your score: {level.score}", True, BLACK)
            screen.blit(score_text, (170, 220))
            level_text = font_middle.render(f"Your level: {level.level}", True, BLACK)
            screen.blit(level_text, (180, 270))
            pygame.display.flip()
            pygame.mixer.Sound('gameover.mp3').play()
            time.sleep(3)
            user.save_userdata(level.score, level.level)
            break
        
        if pygame.time.get_ticks() - food.spawn_time > FOOD_LIFETIME:
            food.respawn(snake.body)
        
        if snake.body[0] == food.pos:
            pygame.mixer.Sound('success.mp3').play()
            level.add_score(food.points)
            food.respawn(snake.body)
        else:
            snake.shrink()

    # draw
    screen.fill(BLACK)
    pygame.draw.rect(screen, (200, 200, 200), pause_button)
    label = font_small.render("Pause" if not paused else "Play", True, BLACK)
    screen.blit(label, (pause_button.x + 20, pause_button.y + 10))

    snake.draw(screen)
    food.draw(screen)
    level.draw(screen)

    if paused:
        pause_label = font_middle.render("PAUSED", True, WHITE)
        screen.blit(pause_label, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
        
    pygame.display.flip()
    clock.tick(level.speed)


user.db.close()
pygame.quit()
