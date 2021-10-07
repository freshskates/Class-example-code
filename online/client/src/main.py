import pygame, sys
# init pygame before importing other dependencies
pygame.init()

from buttons.image_button import ImageButton
from buttons.text import Text
from components.login_form import LoginForm
from game.tictactoe import TicTacToe 

BG_COLOR = (28, 170, 156)

screen = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Game")

clock = pygame.time.Clock()

start_button = ImageButton(screen, 100, 200, "assets/start_btn.png", 0.7)
exit_button = ImageButton(screen, 450, 200, "assets/exit_btn.png", 0.7)

loginform = LoginForm(screen, 100, 300, 200, 45)
user_text = Text(screen, 15, 15, "Not Logged in")
balance_text = Text(screen, 15, 40, "")

# screens below
def game():
    HEIGHT = 600
    WIDTH = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game1 = TicTacToe(screen)
    game1.createBoard()
    click = False
    running = True
    while running: 
        screen.fill(BG_COLOR)

        game1.drawBoard(click)
        
        game1.drawLines(WIDTH, HEIGHT)

        click = False
        for event in pygame.event.get():
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)
        
def main_menu():
    click = False
    run = True
    WIDTH = 800
    HEIGHT = 500
    user_object = {}
    while run: 
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(BG_COLOR)
        
        pos = pygame.mouse.get_pos()
        print(pos)

        start_button.draw()
        exit_button.draw()

        user_text.draw()
        balance_text.draw()
        
        loginform.draw()

        if "success" in user_object:
            user_text.setText(user_object["username"])
            balance_text.setText("Balance: " + str(user_object["balance"]))

        if start_button.collides(pos):
            if click:
                game()
        
        if exit_button.collides(pos):
            if click:
                pygame.quit()
                sys.exit()

        click = False
        for event in pygame.event.get():
            # if not logged in yet
            if "success" not in user_object: 
                user_object = loginform.handle_event(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    click = True

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

main_menu()