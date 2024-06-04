from config import *
import Building_class
from floor_class import *
from elevator_class import *


pygame.init()

# Creating a surface on which to draw
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),vsync=1)
# Creating an object of Building class.
Building = Building_class.Building()
# Creating an image to display in the background.
IMAGE = pygame.image.load('sky.jpg').convert()
rect = IMAGE.get_rect()
rect.bottomleft = (0, 700)



run = True
while run:
    
    # Cleaning the surface by filling it with white.
    screen.fill((255, 255, 255))
    #Drawing the background image.
    screen.blit(IMAGE, rect)

    # Calls an update function in the building class that causes the positions of all elements to be updated.
    Building.update()
    #Calls the build function in the building class which causes all elements to be drawn.
    Building.draw_building(screen)


    #A loop that follows events triggered by the user.
    for event in pygame.event.get():
        #Get an event of the close button being clicked, and close.
        if event.type == pygame.QUIT:
            run = False
        #Get an event of clicking the left mouse button and returns the coordinates of the place of the click.
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            Building.order_elevator(x,y)

    pygame.display.update()

pygame.quit()
