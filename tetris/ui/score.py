import pygame
from tetris.settings import *

class Score:
    def __init__(self, score:int, level:int, lines:int):
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*SCORE_HEIGHT_FRACTION - PADDING))
        self.rect = self.surface.get_rect(bottomright=(WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        self.display_surface = pygame.display.get_surface()
        self.score = 0
        
        #font
        self.font = pygame.font.Font(FONT, FONT_SIZE)
        
        #increment
        self.increment_height = self.surface.get_height() / 3
        
        #data
        self.score = score
        self.level = level
        self.lines = lines

    def update_score(self, score:int, level:int, lines:int):
        self.score=score
        self.level=level
        self.lines=lines

    def _display_text(self, pos, text):
        text_surface = self.font.render(f'{text[0]}: {text[1]}', True,WHITE)
        text_rext = text_surface.get_rect(center=pos)
        self.surface.blit(text_surface, text_rext)
        
    def run(self):
        self.surface.fill(BACKGROUND)

        for i, text in enumerate([('Score', self.score), ('Level', self.level), ('Lines', self.lines)]):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            self._display_text((x,y), text)
            
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)



