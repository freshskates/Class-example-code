import pygame, sys
from game.tictactoe import TicTacToe 

BG_COLOR = (28, 170, 156)

class Game: 

    def __init__(self, name, id):
        self.width = 600
        self.height = 600
        self.setup_screen()

        
        self.game = TicTacToe(self.screen, name, id)

        self.click = False
        self.running = False
        
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.game.draw(self.click)
        self.game.drawLines(self.width, self.height)

        pygame.display.update()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game")

    def run(self):
        self.running = True

        while self.running: 
            self.draw()

            self.click = False
            for event in pygame.event.get():
                self.handle_event(event)

            self.clock.tick(60)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                self.click = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.close_socket()
                self.running = False

        if event.type == pygame.QUIT:
            # disconnect()
            self.game.close_socket()
            pygame.quit()
            sys.exit()

    