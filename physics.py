import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Physics Simulator")
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
running = True
game_paused = False
x_position = 10
y_position = 10
MAX_SPEED = 150 #useless
clock = pygame.time.Clock()
dt = 0.1 #set for the first frame only 0.1

rect_1 = pygame.Rect(100, 100, 30, 30)

font = pygame.font.Font(None, size=30)
font_title = pygame.font.Font(None, size=60)
a_input = 0
d_input = 0
w_input = 0
s_input = 0
x_input = 0
y_input = 0
runtime = 0.0 #total run time in seconds
x_velocity = 0
y_velocity = 0
y_input = 0
force = 15
mass = 1 #kg

def lerp(A, B, alpha):
    return B*alpha + A*(1-alpha)

while running:
    screen.fill((0, 10, 30)) #background
    
    x_velocity += (force * dt * x_input / mass)
    y_velocity += (force * dt * y_input / mass)

    pygame.draw.rect(screen, (255,255,255), rect_1)
    rect_1.topleft = (x_position, y_position)

    if x_position < 1 or x_position > 640-31:
        x_velocity *= -0.8
    if y_position < 1 or y_position > 640-31:
        y_velocity *= -0.8

    x_position = max(0, min(x_position + (x_velocity), 640-30))
    y_position = max(0, min(y_position + (y_velocity), 640-30))

    #render info text for a few seconds
    info_str = font.render("Use 'WASD' keys to move, esc to exit", True, (150, 150, 150))
    info_str.set_alpha(max(0, min(255, 700-runtime*150)))
    screen.blit(info_str, (150, 100))

    #key input detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                d_input = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                d_input = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                a_input = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                a_input = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                w_input = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                w_input = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                s_input = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                s_input = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    #x_input = lerp(x_input, d_input - a_input, dt*2)
    x_input = d_input-a_input
    y_input = s_input-w_input
    

    pygame.display.flip() #render screen
    #delta time
    dt = clock.tick(60) / 1000
    dt = max(1/500, min(1/10, dt))
    runtime += dt

pygame.quit()