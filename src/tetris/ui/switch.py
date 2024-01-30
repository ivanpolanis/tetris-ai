import pygame
from tetris.settings import *


class Switch:
    def __init__(self, screen, rect_position, rect_size, options):
        self.selected_option = 0
        self.rect_position = rect_position
        self.rect_size = rect_size
        self.screen = screen
        self.options = options
        pygame.font.init()
        self.font = pygame.font.Font(FONT, 18)

    def switch_state(self):
        if self.selected_option == 0:
            self.selected_option = 1
        else:
            self.selected_option = 0


    def draw(self):
        half_width = self.rect_size[0] // 2
        left_rect = pygame.Rect(self.rect_position, (half_width, self.rect_size[1]))
        right_rect = pygame.Rect((self.rect_position[0] + half_width, self.rect_position[1]),
                                (half_width, self.rect_size[1]))

        left_color = CHOSEN_OPTION_COLOR if self.selected_option == 0 else UNCHOSEN_OPTION_COLOR
        right_color = CHOSEN_OPTION_COLOR if self.selected_option == 1 else UNCHOSEN_OPTION_COLOR

        pygame.draw.rect(self.screen, left_color, left_rect)
        pygame.draw.rect(self.screen, right_color, right_rect)

        text_left = self.font.render(self.options[0], True, TEXT_COLOR)
        text_right = self.font.render(self.options[1], True, TEXT_COLOR)

        left_text_rect = text_left.get_rect(center=left_rect.center)
        right_text_rect = text_right.get_rect(center=right_rect.center)

        self.screen.blit(text_left, left_text_rect)
        self.screen.blit(text_right, right_text_rect)
        
        return left_rect, right_rect

    def collidepoint(self, point):
        half_width = self.rect_size[0] // 2
        left_rect, right_rect = (pygame.Rect(self.rect_position, (half_width, self.rect_size[1])),
                                pygame.Rect((self.rect_position[0] + half_width, self.rect_position[1]),
                                (half_width, self.rect_size[1])))

        # Check if the click is in the left rectangle
        if left_rect.collidepoint(point):
            if self.selected_option != 0:
                self.switch_state()
            return True

        # Check if the click is in the right rectangle
        elif right_rect.collidepoint(point):
            if self.selected_option != 1:
                self.switch_state()
            return True

        return False
