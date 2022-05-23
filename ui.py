import pygame
from settings import *

class UI:
    def __init__(self):

        # General
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # Bar Setup
        self.health_bar_rect = pygame.Rect()

    def display(self, player):
        pass