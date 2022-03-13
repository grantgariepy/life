import pygame
import random


class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.neighbors = []
        self.alive_neighbors = 0
        self.colour = (0, 0, 0)

    def update(self):
        self.rect.topleft = (self.grid_x*20, self.grid_y*20)

    def draw(self):
        if self.alive:
            self.image.fill((self.colour))
        else:
            self.image.fill((0, 0, 0))
            pygame.draw.rect(self.image, (255, 255, 255), (0, 0, 20, 20))
        self.surface.blit(self.image, (self.grid_x*20, self.grid_y*20))

    def get_neighbors(self, grid):
        neighbor_list = [[1, 1], [-1, -1], [-1, 1], [1, -1], [0, -1], [0, 1], [-1, 0], [1, 0]]
        for neighbor in neighbor_list:
            neighbor[0] += self.grid_x
            neighbor[1] += self.grid_y
        for neighbor in neighbor_list:
            if neighbor[0] < 0:
                neighbor[0] += 60
            if neighbor[1] < 0:
                neighbor[1] += 30
            if neighbor[1] > 29:
                neighbor[1] -= 30
            if neighbor[0] > 59:
                neighbor[0] -= 60
        for neighbor in neighbor_list:
            try:
                self.neighbors.append(grid[neighbor[1]][neighbor[0]])
            except:
                print(neighbor)

    def live_neighbors(self):
        count = 0
        for neighbor in self.neighbors:
            if neighbor.alive:
                count += 1

        self.alive_neighbors = count

    # def set_colour(self):
    #     for cell in self.neighbors:
    #         if cell.colour != (0, 0, 0):
    #             self.colour = cell.colour
    #         else:
    #             self.colour = (random.randint(0, 255), random.randint(
    #                 0, 255),  random.randint(0, 255))
