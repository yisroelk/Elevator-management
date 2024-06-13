from Building import *


pygame.init()


# Creating a surface on which to draw
world = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Creating an object of Building class.
building = Building()
# Set the current window caption.
pygame.display.set_caption("Elevator-management v1.0.0")
# Change the system image for the display window.
img = pygame.image.load(ELEVATOR_IMG)
pygame.display.set_icon(img)


SCROLL_X, SCROLL_Y = 0, WORLD_HEIGHT - SCREEN_HEIGHT
SCROLL_SPEED = 10  # Pixels per key press


run = True
while run:

    # Cleaning the surface by filling it with white.
    world.fill(FILL_COLOR)
    screen.fill(FILL_COLOR)

    # Drawing the background image.
    #screen.blit(background_img, rect)

    # Calls an update function in the building class that causes the positions of all elements to be updated.
    building.update()
    # world.fill((128,128,128))
    # Calls the build function in the building class which causes all elements to be drawn.
    building.draw_building(world)
    screen.blit(world, (0, 0), (SCROLL_X, SCROLL_Y, SCREEN_WIDTH, SCREEN_HEIGHT)) 
    
    # A loop that follows events triggered by the user.
    for event in pygame.event.get():
        # Get an event of the close button being clicked, and close.
        if event.type == pygame.QUIT:
            run = False
        # Get an event of clicking the left mouse button and returns the coordinates of the place of the click.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                SCROLL_Y = max(SCROLL_Y - SCROLL_SPEED, 0)
            elif event.button == 5:  # Scroll down
                SCROLL_Y = min(SCROLL_Y + SCROLL_SPEED, WORLD_HEIGHT - SCREEN_HEIGHT)
            elif event.button == 1:
                x, y = pygame.mouse.get_pos()
                building.order_elevator(x + SCROLL_X, y + SCROLL_Y)

    # Update scroll position based on arrow key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SCROLLOCK]:
        SCROLL_X = max(SCROLL_X - SCROLL_SPEED, 0)
    if keys[pygame.K_RIGHT]:
        SCROLL_X = min(SCROLL_X + SCROLL_SPEED, WORLD_WIDTH - SCREEN_WIDTH)
    if keys[pygame.K_UP]:
        SCROLL_Y = max(SCROLL_Y - SCROLL_SPEED, 0)
    if keys[pygame.K_DOWN]:
        SCROLL_Y = min(SCROLL_Y + SCROLL_SPEED, WORLD_HEIGHT - SCREEN_HEIGHT)
            
    pygame.display.update()

pygame.quit()
