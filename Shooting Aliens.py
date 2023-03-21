import pygame

pygame.init()

# Setting clock
CLOCK = pygame.time.Clock()
dt = 0
FPS = 60  # velocidad de los frames

# Setting Screen
W, H = 600, 480
screen = pygame.display.set_caption("Shooting Aliens")
screen = pygame.display.set_mode((W, H))

# Setting background
image_background = pygame.image.load("img/fondo1.png").convert()
x = 0

# Setting Icon game
icon = pygame.image.load("img/icon/icon-sa.png")
pygame.display.set_icon(icon)

# hero
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

still = pygame.image.load("img/hero/movements/still.png")

walk_right = [pygame.image.load("img/hero/movements/walk-right-1.png"),
              pygame.image.load("img/hero/movements/walk-right-2.png"),
              pygame.image.load("img/hero/movements/walk-right-3.png"),
              pygame.image.load("img/hero/movements/walk-right-4.png"),
              pygame.image.load("img/hero/movements/walk-right-5.png"),
              pygame.image.load("img/hero/movements/walk-right-6.png")]

jump = [
    pygame.image.load("img/hero/movements/jump-1.png"),
    pygame.image.load("img/hero/movements/jump-2.png"),
    pygame.image.load("img/hero/movements/jump-3.png")
]

shoot = [
    pygame.image.load("img/hero/movements/shoot-1.png"),
    pygame.image.load("img/hero/movements/shoot-2.png"),
    pygame.image.load("img/hero/movements/shoot-3.png")
]

hit = [
    pygame.image.load("img/hero/movements/hit.png")
]

die = [
    pygame.image.load("img/hero/movements/die-1.png"),
    pygame.image.load("img/hero/movements/die-2.png")
]

# estados iniciales del hero
is_jumping = False
is_walking_right = False
is_walking_left = False
is_still = True
is_shooting = False
is_dead = False
is_he_hit = False
speed_x = 50
speed_y = 200
steps_counter = 0


def move_player():
    global x
    global steps_counter
    global player_pos

    # background moving
    x_rel = x % screen.get_rect().width
    screen.blit(image_background, (x_rel - image_background.get_rect().width, 0))  # move image
    if x_rel < W and steps_counter:
        screen.blit(image_background, (x_rel, 0))
    x -= 1  # mueve un pixel por frame a la derecha

    # -----
    # verificar si hero excede la pantalla
    if (player_pos.x < 0 or player_pos.x > 600):
        player_pos = -player_pos
    if (player_pos.y < 0 or player_pos.y > 480):
        player_pos.y = -player_pos.y
    # -------
    # mostrar movimientos hero
    # if steps_counter == 0:
    #    screen.blit(still, player_pos)

    # actualiza contador pasos
    if steps_counter + 1 >= 6:
        steps_counter = 0

    # por defecto debe caminar
    if steps_counter >= 0 and steps_counter <= 6:
        screen.blit(walk_right[steps_counter // 1], player_pos)

    if is_jumping:
        screen.blit(jump[steps_counter // 1], player_pos)
        steps_counter += 1 

is_running = True
# Actions & controls loop
while is_running:
    dt = CLOCK.tick(FPS) / 1000  # clock

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # hero movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 50 * dt
        steps_counter += 1
    if keys[pygame.K_s]:
        player_pos.y += 50 * dt
        steps_counter += 1
    if keys[pygame.K_a]:
        player_pos.x -= 50 * dt
        steps_counter += 1
    if keys[pygame.K_d]:
        player_pos.x += 50 * dt
        steps_counter += 1
    if keys[pygame.K_SPACE]:
        player_pos.y += 100 *dt
        is_jumping = True
        steps_counter -= 1 

    pygame.display.update()  # actualizar pantalla
    move_player()  # actualiza movimiento hero

pygame.quit()
