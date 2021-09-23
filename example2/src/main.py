import pygame

pygame.init()

BG_COLOR = (28, 170, 156)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_GREY = (30,30,30)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

def main_menu():
    click = False
    run = True
    WIDTH = 800
    HEIGHT = 500
    circle_x = 0
    circle_y = 250

    color = DARK_GREY
    while run: 
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(BG_COLOR)
        mouse_position = pygame.mouse.get_pos()

        circle = pygame.draw.circle(screen, color, (circle_x, circle_y), 35)
        circle_x = circle_x + 5

        if circle_x == WIDTH:
            circle_x = 0
        
        if circle.collidepoint(mouse_position):
            color = WHITE
        else:
            color = DARK_GREY

        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    click = True

            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
        clock.tick(60)

main_menu()