import pygame
vec = pygame.math.Vector2

class game_window:
    def __init__(self, screen, x, y):
        
        self.pos = vec(x, y)