from config import *
import Building_class
from floor_class import *
from elevator_class import *


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),vsync=1)
Building = Building_class.Building()

run = True
while run:
    
    screen.fill((255, 255, 255))

    Building.update()
    Building.draw_building(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            Building.order_elevator(x,y)
            print(Building.button_pressed(x,y))

    pygame.display.update()

pygame.quit()


# key = pygame.key.get_pressed()
#     if key[pygame.K_a] == True:
#         player.move_ip(-1, 0)
#     elif key[pygame.K_d] == True:
#         player.move_ip(1, 0)
#     elif key[pygame.K_w] == True:
#         player.move_ip(0, -1)
#     elif key[pygame.K_s] == True:
#         player.move_ip(0, 1)