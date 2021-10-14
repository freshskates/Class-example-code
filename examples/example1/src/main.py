import pygame
from buttons.button import Button 

pygame.init()

BG_COLOR = (28, 170, 156)

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

button1 = Button(screen, 0, 0, 200, 100, "Go")

def main_menu():
    click = False
    run = True
    WIDTH = 800
    HEIGHT = 500
    while run: 
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Duality Game")

        screen.fill(BG_COLOR)

        pos = pygame.mouse.get_pos()
        print(pos)
        button1.draw()

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