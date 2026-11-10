import pygame
import pygame_gui

pygame.init()

WINDOW_SIZE = (1000, 900)
BG_COLOR = (148, 193, 209)
TITLE_COLOR = (217, 217, 217)
BTN_W, BTN_H, GAP = 247, 81, 5
GRASS_H = 110

screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Snake Game")

manager = pygame_gui.UIManager(WINDOW_SIZE, "./main/Theme.json")

title_font = pygame.font.Font("./fonts/Itim/Itim-Regular.ttf", 100)
title_surf = title_font.render("Snake Game", True, TITLE_COLOR)


grass = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect(0, -GRASS_H, WINDOW_SIZE[0], GRASS_H),
    manager=manager,
    object_id="#grass",
    anchors={"left": "left", "right": "right", "bottom": "bottom"},
)


col_offset = (BTN_W + GAP) // 2
row1_y = 230
row2_y = row1_y + BTN_H + GAP

def make_button(text, x, y, **anchors):
    return pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(x, y, BTN_W, BTN_H),
        text=text,
        manager=manager,
        anchors={"centerx": "centerx", "top": "top", **anchors},
    )

play_button        = make_button("Play", -col_offset, row1_y)
themes_button      = make_button("Themes", col_offset, row1_y)
infos_button       = make_button("Infos", -col_offset, row2_y)
parameters_button  = make_button("Parameters",col_offset, row2_y)

leaderboard_button = make_button("Leaderboard",  0,          row2_y + BTN_H + GAP + 10)

APPLE_SIZE = 52
apple_surface = pygame.image.load_sized_svg("images/apple.svg", (APPLE_SIZE, APPLE_SIZE))
apple = pygame_gui.elements.UIImage(
    relative_rect=pygame.Rect(-APPLE_SIZE - 60, -GRASS_H - APPLE_SIZE + 3, APPLE_SIZE, APPLE_SIZE),
    image_surface=apple_surface,
    manager=manager,
    anchors={"right": "right", "bottom": "bottom"},
)



def draw_background(surface):
    surface.fill(BG_COLOR)
    w, h = surface.get_size()
    surface.blit(title_surf, title_surf.get_rect(center=(w // 2, 110)))
    

clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            manager.set_window_resolution(event.size)
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == play_button:
                print("Play -> let's start")
            elif event.ui_element == themes_button:
                print("Themes -> change the theme")
            elif event.ui_element == infos_button:
                print("Infos")
            elif event.ui_element == parameters_button:
                print("Parameters")
            elif event.ui_element == leaderboard_button:
                print("Leaderboard")
        manager.process_events(event)

    manager.update(time_delta)
    draw_background(screen)
    manager.draw_ui(screen)
    pygame.display.update()

pygame.quit()