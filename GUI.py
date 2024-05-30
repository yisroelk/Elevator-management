from config import *
import Building_class
from floor_class import *
from elevator_class import *


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),vsync=1)
b = Building_class.Building()
x = 700
y = 700
for i in range (10):
    nu = i
numb = str(nu)

dis = pygame.display.set_mode((x, y))
font = pygame.font.Font('arial.ttf', 12)  
text = font.render(numb, True, (255, 0, 0), None)
text_react = text.get_rect()
text_react.center = (x//2, y//2)

clock = pygame.time.Clock()

run = True
while run:
    
    screen.fill((255, 255, 255))
    # x=0
    # for i in range(0, number_floors+1):
    #     x = x + 60
    #     print(x)
    #     building = pygame.Rect((0, x, 50, 50))

    #pygame.draw.rect(screen, (255, 0, 0), building)
    b.update()
    b.draw_building(screen)
    dis.blit(text, text_react)
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            b.order_elevator(x,y)
            # print(floor_cliced)

    clock.tick(60)
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