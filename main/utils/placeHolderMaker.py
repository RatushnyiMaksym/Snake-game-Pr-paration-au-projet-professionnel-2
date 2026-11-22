
import pygame

def makePlaceholder(size):
    """Image provisoire (gris arrondi). A remplacer plus tard par set_image()."""
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.rect(surf, (217, 217, 217), surf.get_rect(), border_radius=20)
    pygame.draw.rect(surf, (120, 120, 120), surf.get_rect(), width=3, border_radius=20)
    return surf