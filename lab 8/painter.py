import pygame
pygame.init()

# variables
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 125, 246)
PURPLE = (196, 33, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MENU_HEIGHT = 70

# Setting screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Painter")
clock = pygame.time.Clock()

# another variables
drawing = False
start_pos = (0, 0)
current_color = BLACK
brush_size = 5
current_tool = "pen"  # pen, rectangle, circle, eraser
painting = []
# creating separate screen for drawing
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

def draw_menu():
    # menu
    pygame.draw.rect(screen, PINK, [0, 0, WIDTH, MENU_HEIGHT])
    
    # Tools
    pen_btn = pygame.draw.rect(screen, BLACK, [10, 10, 50, 50], 2)
    pygame.draw.line(screen, BLACK, (20, 30), (40, 30), 2)
    
    rect_btn = pygame.draw.rect(screen, BLACK, [70, 10, 50, 50], 2)
    pygame.draw.rect(screen, BLACK, [80, 20, 30, 20], 2)
    
    circle_btn = pygame.draw.rect(screen, BLACK, [130, 10, 50, 50], 2)
    pygame.draw.circle(screen, BLACK, (155, 35), 15, 2)
    
    eraser_btn = pygame.draw.rect(screen, BLACK, [190, 10, 50, 50], 2)
    pygame.draw.rect(screen, WHITE, [200, 20, 30, 20])
    
    # colors
    colors = [
        pygame.draw.rect(screen, RED, [WIDTH-180, 10, 30, 30]),
        pygame.draw.rect(screen, GREEN, [WIDTH-140, 10, 30, 30]),
        pygame.draw.rect(screen, BLUE, [WIDTH-100, 10, 30, 30]),
        pygame.draw.rect(screen, BLACK, [WIDTH-180, 50, 30, 30]),
        pygame.draw.rect(screen, WHITE, [WIDTH-140, 50, 30, 30]),
        pygame.draw.rect(screen, PURPLE, [WIDTH-100, 50, 30, 30])
    ]
    color_values = [RED, GREEN, BLUE, BLACK, WHITE, PURPLE]
    
    # active tool is green
    if current_tool == "pen":
        pygame.draw.rect(screen, GREEN, [10, 10, 50, 50], 3)
    elif current_tool == "rectangle":
        pygame.draw.rect(screen, GREEN, [70, 10, 50, 50], 3)
    elif current_tool == "circle":
        pygame.draw.rect(screen, GREEN, [130, 10, 50, 50], 3)
    elif current_tool == "eraser":
        pygame.draw.rect(screen, GREEN, [190, 10, 50, 50], 3)
    
    return [pen_btn, rect_btn, circle_btn, eraser_btn], colors, color_values

def draw_painting():
    canvas.fill(WHITE) #clear canvas
    # painting with every tool
    for item in painting:
        color, start, end, tool, width = item
        if tool == "pen":
            pygame.draw.line(canvas, color, start, end, width)
        elif tool == "rectangle":
            rect = pygame.Rect(start, (end[0]-start[0], end[1]-start[1]))
            pygame.draw.rect(canvas, color, rect, width)
        elif tool == "circle":
            radius = int(((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5)
            pygame.draw.circle(canvas, color, start, radius, width)
        elif tool == "eraser": 
            if end[1] > MENU_HEIGHT: # erase below menu
                pygame.draw.circle(canvas, WHITE, end, width)
    
    screen.blit(canvas, (0, 0)) # drawing canvas to screen

running = True
while running:
    mouse_pos = pygame.mouse.get_pos() #getting mouse position
    
    # painting
    screen.fill(WHITE) #clear screen
    draw_painting()
    tool_buttons, color_buttons, color_values = draw_menu()
    
    # painting on screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #drawing following the mouse motion
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos[1] > MENU_HEIGHT: #only below menu
                drawing = True
                start_pos = mouse_pos
                if current_tool == "pen":
                    painting.append((current_color, mouse_pos, mouse_pos, "pen", brush_size))
                elif current_tool == "eraser":
                    painting.append((WHITE, mouse_pos, mouse_pos, "eraser", brush_size*2))
            else:
                # check tool buttons
                for i, btn in enumerate(tool_buttons):
                    if btn.collidepoint(mouse_pos):
                        if i == 0: current_tool = "pen"
                        elif i == 1: current_tool = "rectangle"
                        elif i == 2: current_tool = "circle"
                        elif i == 3: current_tool = "eraser"
                
                # check color buttons
                for i, btn in enumerate(color_buttons):
                    if btn.collidepoint(mouse_pos):
                        current_color = color_values[i]
        
        if event.type == pygame.MOUSEMOTION and drawing:
            if mouse_pos[1] > MENU_HEIGHT:
                if current_tool == "pen":
                    painting.append((current_color, painting[-1][2], mouse_pos, "pen", brush_size))
                elif current_tool == "eraser":
                    painting.append((WHITE, painting[-1][2], mouse_pos, "eraser", brush_size*2))
        
        if event.type == pygame.MOUSEBUTTONUP and drawing:
            drawing = False
            if mouse_pos[1] > MENU_HEIGHT:
                if current_tool == "rectangle":
                    painting.append((current_color, start_pos, mouse_pos, "rectangle", brush_size))
                elif current_tool == "circle":
                    painting.append((current_color, start_pos, mouse_pos, "circle", brush_size))
        
        # mouse btn release
        if event.type == pygame.MOUSEBUTTONUP and drawing:
            drawing = False
            if mouse_pos[1] > MENU_HEIGHT:  # only draw below menu
                if current_tool == "rectangle":
                    painting.append((current_color, start_pos, mouse_pos, "rectangle", brush_size))
                elif current_tool == "circle":
                    painting.append((current_color, start_pos, mouse_pos, "circle", brush_size))    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                painting=[]
                canvas.fill(WHITE) # clearing the drawings
    # preview
    if drawing and current_tool in ["rectangle", "circle"] and mouse_pos[1] > MENU_HEIGHT:
        temp_surface = canvas.copy()
        if current_tool == "rectangle":
            rect = pygame.Rect(start_pos, (mouse_pos[0]-start_pos[0], mouse_pos[1]-start_pos[1]))
            pygame.draw.rect(temp_surface, current_color, rect, 1)
        elif current_tool == "circle":
            radius = int(((mouse_pos[0]-start_pos[0])**2 + (mouse_pos[1]-start_pos[1])**2)**0.5)
            pygame.draw.circle(temp_surface, current_color, start_pos, radius, 1)
        screen.blit(temp_surface, (0, 0))
        draw_menu()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()