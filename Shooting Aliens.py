import pygame

pygame.init()

# Setting clock
CLOCK = pygame.time.Clock()

is_running = True
dt = 0
FPS = 60 # velocidad de los frames

# Setting Screen
W, H = 600, 480
screen = pygame.display.set_caption("Shooting Aliens")
screen = pygame.display.set_mode((W,H))

# Setting background
image_background = pygame.image.load("img/fondo1.png").convert()
x = 0

# Setting Icon game
icon = pygame.image.load("img/icon/icon-sa.png")
pygame.display.set_icon(icon)


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False   
    
    # hero movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # permite que avance correctamente la animacion del fondo
    x_rel = x % screen.get_rect().width
    screen.blit(image_background, (x_rel - image_background.get_rect().width, 0)) # move image
    if x_rel < W:
        screen.blit(image_background, (x_rel, 0))
    
    # ---------------
    x -= 1 # mueve un pixel por frame a la derecha

    pygame.display.update() # actualizar pantalla

    dt = CLOCK.tick(FPS) / 1000

pygame.quit()