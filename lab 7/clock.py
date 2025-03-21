import pygame
import math
import datetime

# Инициализация pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 840, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

# Загрузка изображений
background = pygame.image.load("/Users/uldanakonyratbaeva/Desktop/lab 7/mickey.JPG")  # Лицо Микки Мауса
right_hand = pygame.image.load("/Users/uldanakonyratbaeva/Desktop/lab 7/right hand.PNG")   # Правая рука (секунды)
left_hand = pygame.image.load("/Users/uldanakonyratbaeva/Desktop/lab 7/left hand.PNG")     # Левая рука (минуты)

# Изменение размера изображений
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
right_hand = pygame.transform.scale(right_hand, (190, 126))
left_hand = pygame.transform.scale(left_hand, (130, 107))

# Функция для отрисовки руки
def draw_hand(image, angle, length):
    rotated_hand = pygame.transform.rotate(image, angle)
    rect = rotated_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    offset_x = math.cos(math.radians(angle)) * length
    offset_y = math.sin(math.radians(angle)) * length
    screen.blit(rotated_hand, (rect.x + offset_x, rect.y - offset_y))

# Основной цикл
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    
    # Получаем текущее время
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute
    
    # Вычисляем углы вращения рук
    second_angle = -seconds * 6  # 360 / 60 = 6 градусов на секунду
    minute_angle = -minutes * 6  # 360 / 60 = 6 градусов на минуту
    
    # Отрисовываем руки
    draw_hand(left_hand, minute_angle, 50)
    draw_hand(right_hand, second_angle, 70)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
