import pygame
from tetris.ui.switch import Switch
from tetris.settings import *
import random



def create_new_block(sprites):
    new_block = Pregame_Block(random.choice(list(TETROMINOS.keys())), sprites)
    sprites.add(new_block)

class Pregame:
    def __init__(self, screen, clock):
        self.size = 4
        self.screen = screen
        self.clock = clock
        self.switch = Switch(self.screen, (WINDOW_WIDTH/2-80, WINDOW_HEIGHT/2 + 335), (150, 40), ["User", "AI"])
        self.waiting_for_start = True
        self.user_mode = True


    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                if (self.start_rect.collidepoint(event.pos)):
                    self.waiting_for_start = False
                elif self.switch.collidepoint(event.pos):
                    self.user_mode = (self.switch.selected_option == 0)


    def _draw_elements(self):
        pygame.draw.rect(self.screen, pygame.Color(PREGAME_BACKGROUND), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        
        current_time = pygame.time.get_ticks()
        if current_time % BLOCK_CREATION_INTERVAL == 0:
            create_new_block(self.block_group)
        self.block_group.draw(self.screen)

        title_image = pygame.image.load(TITLE_PATH)
        title_rect = title_image.get_rect()
        title_rect.center = (WINDOW_WIDTH/2, 150)
        self.screen.blit(title_image, title_rect)

        
        #Start Game
        font = pygame.font.Font(FONT, 20)
        self.start_rect = pygame.Rect(WINDOW_WIDTH/2-143, 715, 280, 50)
        pygame.draw.rect(self.screen, START_BUTTON_COLOR, self.start_rect, border_radius=3)
        start_text = font.render("Start Game", True, WHITE)
        start_text_rect = start_text.get_rect(center=(self.start_rect.centerx, self.start_rect.centery))
        self.screen.blit(start_text, start_text_rect)
        
        # User mode vs AI mode
        self.switch.draw()


    def run(self) -> bool:
        self.block_group = pygame.sprite.Group()
        while self.waiting_for_start:
            self.block_group.update()
            self._draw_elements()
            self._handle_events()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.draw.rect(self.screen, pygame.Color(BACKGROUND), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        return self.user_mode



class Pregame_Block(pygame.sprite.Sprite):
    def __init__(self, tetromino_key, sprites):
        super().__init__()
        self.sprites = sprites
        self.image = pygame.image.load(TETROMINOS[tetromino_key]['color']).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - BLOCK_SIZE)
        self.rect.y = -BLOCK_SIZE

    def update(self):
        self.rect.y += BLOCK_FALL_SPEED
        if self.rect.y > WINDOW_HEIGHT:
            self.kill()
            create_new_block(self.sprites)
