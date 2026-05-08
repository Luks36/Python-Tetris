import pygame as pg

pg.init()

clock = pg.time.Clock()
block_size = 30
colums = 10
rows = 20
width = colums * block_size
height = rows * block_size
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Tetris")

def grid(surface):
    for x in range(0, width, block_size):
        pg.draw.line(surface, (40, 40, 40), (x, 0), (x, height))
    for y in range(0, height, block_size):
        pg.draw.line(surface, (40, 40, 40), (0, y), (width, y))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0, 0, 0))
    grid(screen)
    pg.display.flip()
    clock.tick(60)

pg.quit()