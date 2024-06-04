from config import *
import Building_class
from floor_class import *
from elevator_class import *


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),vsync=1)
Building = Building_class.Building()
IMAGE = pygame.image.load('sky.jpg').convert()
# Create a rect with the size of the image.
rect = IMAGE.get_rect()
rect.bottomleft = (0, 700)

run = True
while run:
    
    screen.fill((255, 255, 255))
    screen.blit(IMAGE, rect)

    Building.update()
    Building.draw_building(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            Building.order_elevator(x,y)

    pygame.display.update()

pygame.quit()
