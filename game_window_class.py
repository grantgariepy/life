import pygame
from cell_class import *
import copy
vec = pygame.math.Vector2


class Game_window:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = vec(x, y)
        self.width, self.height = 1200, 600
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rows = 30
        self.cols = 60
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)] for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbors(self.grid)

    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()

    def draw(self):
        self.image.fill((0, 0, 0))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))

    def reset_grid(self):
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)] for y in range(self.rows)]

    def evaluate(self):
        new_grid = copy.copy(self.grid)

        for row in self.grid:
            for cell in row:
                cell.live_neighbors()

        for yidx, row in enumerate(self.grid):
            for xidx, cell in enumerate(row):
                if cell.alive:
                    if cell.alive_neighbors == 2 or cell.alive_neighbors == 3:
                        new_grid[yidx][xidx].alive = True
                    if cell.alive_neighbors < 2:
                        new_grid[yidx][xidx].alive = False
                    if cell.alive_neighbors > 3:
                        new_grid[yidx][xidx].alive = False
                else:
                    if cell.alive_neighbors == 3:
                        new_grid[yidx][xidx].alive = True

        # for yidx, row in enumerate(self.grid):
        #     for xidx, cell in enumerate(row):
        #         if cell.alive:
        #             new_grid[yidx][xidx].set_colour()

        self.grid = new_grid
