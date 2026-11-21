import random
import pygame


class Fruit:
    def __init__(self, cell_size=20):
        self.position = None
        self.cell_size = cell_size

    def get_position(self):
        return self.position

    def spawn(self, map, occupied_positions):
        occupied = set(occupied_positions)

        free_cells = [
            (x, y)
            for x in range(map.get_width())
            for y in range(map.get_height())
            if (x, y) not in occupied and not map.is_obstacle((x, y))
        ]

        if not free_cells:
            self.position = None
            return False

        self.position = random.choice(free_cells)
        return True

    def draw(self, screen):
        if self.position is None:
            return
        x, y = self.position
        rect = (x * self.cell_size, y * self.cell_size,
                self.cell_size, self.cell_size)
        pygame.draw.rect(screen, (220, 40, 40), rect)