import pygame
from config import *
import Building_class


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
b = Building_class.Building()
x = 700
y = 700
dis = pygame.display.set_mode((x, y))
font = pygame.font.Font('arial.ttf', 12)
text = font.render('10', True, (255, 0, 0), None)
text_react = text.get_rect()
text_react.center = (x//2, y//2)

run = True
while run:

    screen.fill((255, 255, 255))
    # x=0
    # for i in range(0, number_floors+1):
    #     x = x + 60
    #     print(x)
    #     building = pygame.Rect((0, x, 50, 50))

    #pygame.draw.rect(screen, (255, 0, 0), building)
    b.draw_building(screen)
    dis.blit(text, text_react)
    


    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            floor_clicked = b.conversion_button(x, y)
            # print(floor_cliced)




    pygame.display.update()

pygame.quit()

