import pygame, sys
from screens.game_screen import Game

from buttons.image_button import ImageButton
from components.login_form import LoginForm
from components.register_form import RegisterForm
from buttons.text import Text
from buttons.input_box import InputBox

BG_COLOR = (28, 170, 156)

class MainScreen: 

    def __init__(self):
        self.width = 800
        self.height = 500
        self.setup_screen()

        # objects init
        start_button = ImageButton(self.screen, 100, 200, "assets/start_btn.png", 0.7)
        exit_button = ImageButton(self.screen, 450, 200, "assets/exit_btn.png", 0.7)
        exit_button = ImageButton(self.screen, 450, 200, "assets/exit_btn.png", 0.7)
        user_text = Text(self.screen, 15, 15, "Not Logged in")
        balance_text = Text(self.screen, 15, 40, "")
        self.login_form = LoginForm(self.screen, 100, 300, 200, 45)
        self.register_form = RegisterForm(self.screen, 450, 300, 200, 45)
        self.game_id_box = InputBox(self.screen, 100, 300 + 55, 200, 45)
        
        self.components = { "start": start_button, "exit": exit_button, "user_text": user_text, "balance_text": balance_text }

        self.click = False
        self.running = True

        # once user is logged in, user object will contain user information
        self.user_object = {}
        
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill(BG_COLOR)

        for component in self.components.values():
            component.draw()

        if self.user_object:
            self.game_id_box.draw()

        self.login_form.draw()
        self.register_form.draw()
        pygame.display.update()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Menu")

    def run(self):
        
        while self.running: 
            pos = pygame.mouse.get_pos()
            
            print(pos)

            self.draw()

            # if user successfully logged in
            temp_user = ""
            temp_balance = ""

            if self.user_object:
                temp_user = self.user_object["username"]
                temp_balance = "Balance: " + str(self.user_object["balance"])

            self.components["user_text"].setText(temp_user)
            self.components["balance_text"].setText(temp_balance)                

            if self.components["start"].collides(pos):
                if self.click and self.user_object:
                    player_name = self.user_object["username"]
                    custom_game_id = self.game_id_box.getText()
                    
                    # if no room id entered, start new game
                    if len(custom_game_id) == 0:
                        custom_game_id = None
                    
                    Game(player_name, custom_game_id).run()

                    # self.setup_screen is to reset screen dimensions and window settings 
                    # after the other window closes
                    self.setup_screen()

            if self.components["exit"].collides(pos):
                if self.click:
                    pygame.quit()
                    sys.exit()

            self.click = False
            for event in pygame.event.get():
                self.handle_event(event)

            self.clock.tick(60)

    def handle_event(self, event):
        # if not logged in yet
        # if "success" not in self.user_object: 
        self.register_form.handle_event(event)

        self.user_object = self.login_form.handle_event(event)

        self.game_id_box.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                self.click = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    