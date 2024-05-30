from config import *
# from Building_class import *
# from elevator_class import *
# from GUI import *


class floor:

    def __init__(self, i):
        self.timer = 0              # "return to here"
        self.num_floor = i
        # background
        

    def draw_floor(self, screen):
        y = (self.num_floor*FLOOR_HEIGHT)+5 # ""FIX THE POSITION!!""
        floor = pygame.Rect((BUILDING_POSITION_WIDTH, y, FLOOR_WIDTH, FLOOR_HEIGHT))
        pygame.draw.rect(screen, (0, 187, 255), floor)
        pygame.draw.line(screen,(0, 0, 0),(BUILDING_POSITION_WIDTH, y+3),(BUILDING_POSITION_WIDTH + FLOOR_WIDTH-1 ,y+3),7)


    def draw_button(self, screen):
        y = (self.num_floor*FLOOR_HEIGHT)+5 # ""FIX THE POSITION!!""
        butoon = pygame.Rect((BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) , y+8, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(screen, (0, 255, 0), butoon)

    
    def drew_number(self, screen):
        y = (self.num_floor*FLOOR_HEIGHT) # ""FIX THE POSITION!!""
        number = str(self.num_floor)
        font = pygame.font.Font('arial.ttf', 12)
        text = font.render(number, True, (0, 0, 255), None)
        text_react = text.get_rect()
        text_react.center = (BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2, y)

        
    def elevator_arrive(self, time):
        self.timer = time


    def timer_draw(self, timer):
        pass




