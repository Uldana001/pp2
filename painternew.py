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
    
    # New shape buttons
    square_btn = pygame.draw.rect(screen, BLACK, [250, 10, 50, 50], 2)
    pygame.draw.rect(screen, BLACK, [260, 20, 30, 30], 2)  # Square icon
    
    right_triangle_btn = pygame.draw.rect(screen, BLACK, [310, 10, 50, 50], 2)
    pygame.draw.polygon(screen, BLACK, [(320, 40), (350, 40), (320, 20)], 2)  # Right triangle icon
    
    equilateral_triangle_btn = pygame.draw.rect(screen, BLACK, [370, 10, 50, 50], 2)
    pygame.draw.polygon(screen, BLACK, [(380, 40), (420, 40), (400, 20)], 2)  # Equilateral triangle icon
    
    rhombus_btn = pygame.draw.rect(screen, BLACK, [430, 10, 50, 50], 2)
    pygame.draw.polygon(screen, BLACK, [(440, 35), (455, 20), (480, 35), (455, 50)], 2)  
    
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
    
    # Highlight active tool 
    active_tools = {
        "pen": [10, 10, 50, 50],
        "rectangle": [70, 10, 50, 50],
        "circle": [130, 10, 50, 50],
        "eraser": [190, 10, 50, 50],
        "square": [250, 10, 50, 50],
        "right_triangle": [310, 10, 50, 50],
        "equilateral_triangle": [370, 10, 50, 50],
        "rhombus": [430, 10, 50, 50]
    }
    if current_tool in active_tools:
        pygame.draw.rect(screen, GREEN, active_tools[current_tool], 3)
    
    return [pen_btn, rect_btn, circle_btn, eraser_btn, square_btn, right_triangle_btn, equilateral_triangle_btn, rhombus_btn], colors, color_values


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
        # New shape drawing logic
        elif tool == "square":
            size = max(abs(end[0]-start[0]), abs(end[1]-start[1]))
            rect = pygame.Rect(start, (size, size))
            pygame.draw.rect(canvas, color, rect, width)
        elif tool == "right_triangle":
            points = [start, (end[0], start[1]), end]
            pygame.draw.polygon(canvas, color, points, width)
        elif tool == "equilateral_triangle":
            height = end[1] - start[1]
            base_half = height * (3**0.5)/3  # Equilateral triangle proportions
            points = [
                start,
                (start[0] - base_half, end[1]),
                (start[0] + base_half, end[1])
            ]
            pygame.draw.polygon(canvas, color, points, width)
        elif tool == "rhombus":
            center_x = (start[0] + end[0]) // 2
            center_y = (start[1] + end[1]) // 2
            width_rhombus = abs(end[0] - start[0])
            height_rhombus = abs(end[1] - start[1])
            points = [
                (center_x, start[1]),  # Top point
                (end[0], center_y),    # Right point
                (center_x, end[1]),    # Bottom point
                (start[0], center_y)   # Left point
            ]
            pygame.draw.polygon(canvas, color, points, width)
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
                        tools = ["pen", "rectangle", "circle", "eraser", "square", 
                                "right_triangle", "equilateral_triangle", "rhombus"]
                        current_tool = tools[i]
                
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
                elif current_tool == "square":
                    painting.append((current_color, start_pos, mouse_pos, "square", brush_size))
                elif current_tool == "right_triangle":
                    painting.append((current_color, start_pos, mouse_pos, "right_triangle", brush_size))
                elif current_tool == "equilateral_triangle":
                    painting.append((current_color, start_pos, mouse_pos, "equilateral_triangle", brush_size))
                elif current_tool == "rhombus":
                    painting.append((current_color, start_pos, mouse_pos, "rhombus", brush_size))


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                painting=[]
                canvas.fill(WHITE) # clearing the drawings
    # preview
    if drawing and current_tool in ["rectangle", "circle", "square", "right_triangle", 
                                  "equilateral_triangle", "rhombus"] and mouse_pos[1] > MENU_HEIGHT:
        temp_surface = canvas.copy()
        if current_tool == "rectangle":
            rect = pygame.Rect(start_pos, (mouse_pos[0]-start_pos[0], mouse_pos[1]-start_pos[1]))
            pygame.draw.rect(temp_surface, current_color, rect, 1)
        elif current_tool == "circle":
            radius = int(((mouse_pos[0]-start_pos[0])**2 + (mouse_pos[1]-start_pos[1])**2)**0.5)
            pygame.draw.circle(temp_surface, current_color, start_pos, radius, 1)
        elif current_tool == "square":
            size = max(abs(mouse_pos[0]-start_pos[0]), abs(mouse_pos[1]-start_pos[1]))
            rect = pygame.Rect(start_pos, (size, size))
            pygame.draw.rect(temp_surface, current_color, rect, 1)
        elif current_tool == "right_triangle":
            points = [start_pos, (mouse_pos[0], start_pos[1]), mouse_pos]
            pygame.draw.polygon(temp_surface, current_color, points, 1)
        elif current_tool == "equilateral_triangle":
            height = mouse_pos[1] - start_pos[1]
            base_half = height * (3**0.5)/3
            points = [
                start_pos,
                (start_pos[0] - base_half, mouse_pos[1]),
                (start_pos[0] + base_half, mouse_pos[1])
            ]
            pygame.draw.polygon(temp_surface, current_color, points, 1)
        elif current_tool == "rhombus":
            center_x = (start_pos[0] + mouse_pos[0]) // 2
            center_y = (start_pos[1] + mouse_pos[1]) // 2
            width_rhombus = abs(mouse_pos[0] - start_pos[0])
            height_rhombus = abs(mouse_pos[1] - start_pos[1])
            points = [
                (center_x, start_pos[1]),
                (mouse_pos[0], center_y),
                (center_x, mouse_pos[1]),
                (start_pos[0], center_y)
            ]
            pygame.draw.polygon(temp_surface, current_color, points, 1)

        screen.blit(temp_surface, (0, 0))
        draw_menu()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()