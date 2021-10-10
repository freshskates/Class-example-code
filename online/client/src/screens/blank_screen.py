import pygame, sys
from buttons.button import Button

BG_COLOR = (30, 30, 30)
BLACK_COLOR = (0,0,0)
class Blank: 

    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.setup_screen()

        self.click = False
        self.running = True
                
        self.button = Button(self.screen, self.width//2 - 100, self.height//2 - 25, 200, 50, "BLANK SCREEN", BLACK_COLOR)

        self.clock = pygame.time.Clock()


    def draw(self):
        self.screen.fill(BG_COLOR)

        self.button.draw()

        pygame.display.update()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Blank Template Screen")


    def run(self):
        while self.running: 
            pos = pygame.mouse.get_pos()

            self.draw()
            if self.button.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")

            self.click = False
            for event in pygame.event.get():
                self.handle_events(event)

            self.clock.tick(60)


    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                self.click = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()