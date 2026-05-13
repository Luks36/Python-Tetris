import pygame
import random

# 1. Setup & Variablen
pygame.init()
screen = pygame.display.set_mode((300, 600))
clock = pygame.time.Clock()

# Spielfeld: 20 Zeilen mit je 10 Nullen (0 = leer)
grid = [[0 for _ in range(10)] for _ in range(20)]

# Formen (Shapes): X,Y Koordinaten für I, O, T, S
SHAPES = [
    [(0,0), (0,-1), (0,1), (0,2)], [(0,0), (1,0), (0,1), (1,1)],
    [(0,0), (-1,0), (1,0), (0,-1)], [(0,0), (-1,0), (0,-1), (1,-1)]
]

def check_collision(pos, shape):
    for dx, dy in shape:
        x, y = pos[0] + dx, pos[1] + dy
        if x < 0 or x >= 10 or y >= 20 or (y >= 0 and grid[y][x]):
            return True
    return False

# Start-Zustand
cur_shape = random.choice(SHAPES)
cur_pos = [5, 0]
drop_timer = 0

# 2. Hauptschleife
running = True
while running:
    screen.fill((0, 0, 0)) # Schwarz
    drop_timer += clock.get_rawtime()
    clock.tick()

    # Events (Tastatur)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not check_collision([cur_pos[0]-1, cur_pos[1]], cur_shape): cur_pos[0] -= 1
            if event.key == pygame.K_RIGHT:
                if not check_collision([cur_pos[0]+1, cur_pos[1]], cur_shape): cur_pos[0] += 1
            if event.key == pygame.K_UP:
                rotated = [(y, -x) for x, y in cur_shape]
                if not check_collision(cur_pos, rotated): cur_shape = rotated

    # Automatisches Fallen
    if drop_timer > 500:
        if not check_collision([cur_pos[0], cur_pos[1]+1], cur_shape):
            cur_pos[1] += 1
        else:
            # Stein festfrieren
            for dx, dy in cur_shape:
                grid[cur_pos[1]+dy][cur_pos[0]+dx] = 1
            # Reihen löschen
            grid = [row for row in grid if 0 in row]
            while len(grid) < 20: grid.insert(0, [0]*10)
            # Neuer Stein
            cur_pos, cur_shape = [5, 0], random.choice(SHAPES)
            if check_collision(cur_pos, cur_shape): running = False # Verloren
        drop_timer = 0

    # 3. Zeichnen
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val: pygame.draw.rect(screen, (255,0,0), (x*30, y*30, 29, 29))
    
    for dx, dy in cur_shape:
        pygame.draw.rect(screen, (255,255,255), ((cur_pos[0]+dx)*30, (cur_pos[1]+dy)*30, 29, 29))

    pygame.display.flip()

pygame.quit()
