import pygame
vec = pygame.math.Vector2

class Game_window:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = vec(x, y)
        self.width, self.height = 500, 500
        self.image = pygameSurface((self.width, self.height))
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.topleft = self.pos

    def draw(self):
        self.image.fill((0,0,0))
        self.screen.blit(slef.image, (self.pos.x, self.pos.y))
