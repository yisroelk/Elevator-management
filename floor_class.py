from config import *
# from Building_class import *
# from elevator_class import *
# from GUI import *
from timer_class import *


class floor:

    def __init__(self, i):
        self.timer = Timer(0)   
        self.timer_color = Timer(0)          
        self.num_floor = i
        self.floor_available = True
        self.dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
        

    def draw_floor(self, screen):
        y = (self.num_floor*FLOOR_HEIGHT) # ""FIX THE POSITION!!""
        floor = pygame.Rect((BUILDING_POSITION_WIDTH, y, FLOOR_WIDTH, FLOOR_HEIGHT))
        pygame.draw.rect(screen, (0, 187, 255), floor)
        pygame.draw.line(screen,(0, 0, 0),(BUILDING_POSITION_WIDTH, y+3),(BUILDING_POSITION_WIDTH + FLOOR_WIDTH-1 ,y+3),7)


    def draw_button(self, screen):
        y = (self.num_floor*FLOOR_HEIGHT) # ""FIX THE POSITION!!""
        butoon = pygame.Rect((BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) , y+9, BUTTON_WIDTH, BUTTON_HEIGHT))
        if self.timer_color.time_remaining() > 0:
            pygame.draw.rect(screen, (255, 0, 0), butoon)
        else:
            pygame.draw.rect(screen, (0, 255, 0), butoon)

    
    def drew_number(self, dis):
        y = (self.num_floor*FLOOR_HEIGHT + (FLOOR_HEIGHT//2) + 4)
        number = str(self.num_floor)
        font = pygame.font.Font('arial.ttf', 12)
        text = font.render(number, True, (0, 0, 255), None)
        text_react = text.get_rect()
        text_react.center = (BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2, y)
        dis.blit(text, text_react)

    def draw_timer(self, dis):
        y = (self.num_floor*FLOOR_HEIGHT + (FLOOR_HEIGHT//2) + 4)
        time_remaining = self.timer.time_remaining()
        if time_remaining > 0:
            a = f'{time_remaining:.2f}'
            font = pygame.font.Font('arial.ttf', 12)
            text = font.render(a, True, (0, 0, 255), None)
            text_react = text.get_rect()
            text_react.center = (BUILDING_POSITION_WIDTH + FLOOR_WIDTH//4, y)
            dis.blit(text, text_react)

        
    def elevator_arrive(self, time):
        self.timer = Timer(time)
        self.timer_color = Timer(time + TIME_STOP_FLOOR)

    def draw_building(self, screen):
        self.draw_floor(screen)
        self.draw_button(screen)
        self.drew_number(self.dis)
        self.draw_timer(self.dis)
    
    def update_floor_availability(self):
        if self.timer_color.time_remaining() > 0:
            self.floor_available = False
        else:
            self.floor_available = True
        return self.floor_available






