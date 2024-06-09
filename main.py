from Building import *


pygame.init()

# Creating a surface on which to draw
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),vsync = 1)
# Creating an object of Building class.
building = Building()
# Creating an image to display in the background.
background_img = pygame.image.load(BACKGROUND_IMG).convert()
rect = background_img.get_rect()
rect.bottomleft = (0, SCREEN_HEIGHT)
# Set the current window caption.
pygame.display.set_caption("Elevator-management v1.0.0")
# Change the system image for the display window.
img = pygame.image.load(ELEVATOR_IMG)
pygame.display.set_icon(img)



run = True
while run:
    
    # Cleaning the surface by filling it with white.
    screen.fill((255, 255, 255))
    #Drawing the background image.
    screen.blit(background_img, rect)


    # Calls an update function in the building class that causes the positions of all elements to be updated.
    building.update()
    #Calls the build function in the building class which causes all elements to be drawn.
    building.draw_building(screen)


    #A loop that follows events triggered by the user.
    for event in pygame.event.get():
        #Get an event of the close button being clicked, and close.
        if event.type == pygame.QUIT:
            run = False
        #Get an event of clicking the left mouse button and returns the coordinates of the place of the click.
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            building.order_elevator(x, y)
            

    pygame.display.update()

pygame.quit()
