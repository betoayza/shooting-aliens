import pygame

pygame.init()

# Setting clock
CLOCK = pygame.time.Clock()
dt = 0
FPS = 60  # frames speed

# Setting SCREEN
W, H = 600, 480
SCREEN = pygame.display.set_caption("Shooting Aliens")
SCREEN = pygame.display.set_mode((W, H))

# Setting wallpaper
WALLPAPER = pygame.image.load("img/fondo1.png")
x = 0

# Setting icon game
icon = pygame.image.load("img/icon/icon-sa.png")
pygame.display.set_icon(icon)

# hero's images
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

# hero initial states
player_position = pygame.Vector2(0,300)
is_jumping = False
steps_counter = 0
is_walking = False
speed = 200 # moving 200 pixels by type

def move_player():
    global x
    global steps_counter
    global player_position  
    global is_jumping  

    # BACKGROUND MOVEMENT
    x_rel = x % SCREEN.get_rect().width
    SCREEN.blit(WALLPAPER,
                (x_rel - WALLPAPER.get_rect().width, 0))  # move image
    if x_rel < W:
        SCREEN.blit(WALLPAPER, (x_rel, 0))

    x -= 1  # move 1 pixel to left

    # -----
    # hero screen limits
    if player_position.x <= 0 or player_position.x >= 550:
        player_position.x = -player_position.x
    if player_position.y <= 200 or player_position.y >= 350:
        player_position.y = -player_position.y

    # -------
    # HERO MOVEMENTS by steps counter

    # reset steps
    if steps_counter + 1 >= 7:
        steps_counter = 0     

    # if jumping is finished
    if is_jumping and steps_counter == 3:
        is_jumping = False
        steps_counter = 0   

    if steps_counter >= 0:
        if is_jumping and steps_counter <= 2:
            SCREEN.blit(jump[steps_counter // 1], player_position)        
            steps_counter += 1                        
        if is_walking:
            SCREEN.blit(walk_right[steps_counter // 1], player_position)            
        if steps_counter == 0:
            SCREEN.blit(still, player_position)


# Game & controls loop
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # game clock in seconds
    dt = CLOCK.tick(FPS) / 1000  

    # controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_position.y -= speed * dt
        steps_counter += 1
        is_jumping = False
        is_walking = True        

    if keys[pygame.K_s]:
        player_position.y += speed * dt    
        steps_counter += 1   
        is_jumping = False
        is_walking = True

    if keys[pygame.K_a]:
        player_position.x -= speed * dt     
        steps_counter += 1   
        is_jumping = False
        is_walking = True

    if keys[pygame.K_d]:
        player_position.x += speed * dt
        steps_counter += 1
        is_jumping = False
        is_walking = True

    if keys[pygame.K_SPACE]:
        player_position.y -= 200 * dt  
        steps_counter = 0
        is_jumping = True
        is_walking = False        

    pygame.display.update()    
    move_player() 

pygame.quit()
