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
        y = (SCREEN_HEIGHT - (self.num_floor+1)*FLOOR_HEIGHT)
        # floor = pygame.Rect((BUILDING_POSITION_WIDTH, y, FLOOR_WIDTH, FLOOR_HEIGHT))
        image = pygame.image.load("brick.jpg").convert()
        # pygame.draw.rect(screen, (0, 187, 255), floor)
        screen.blit(image, (BUILDING_POSITION_WIDTH, y), (0,0, FLOOR_WIDTH, FLOOR_HEIGHT))
        pygame.draw.line(screen,(0, 0, 0),(BUILDING_POSITION_WIDTH, y+3),(BUILDING_POSITION_WIDTH + FLOOR_WIDTH-1 ,y+3),7)


    def draw_button(self, screen):
        y = ( SCREEN_HEIGHT - (self.num_floor+1)*FLOOR_HEIGHT + ((FLOOR_HEIGHT+BUTTOM_SPACE)/2))
        #y = (SCREEN_HEIGHT - (self.num_floor+1)*FLOOR_HEIGHT)
        butoon = pygame.Rect((BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) , y+9, BUTTON_WIDTH, BUTTON_HEIGHT))
        if self.timer_color.time_remaining() > 0:
            pygame.draw.circle(screen, BUTTON_PRESSED_COLOR, ((BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2), y), 10)
            #pygame.draw.rect(screen, BUTTON_PRESSED_COLOR, butoon)
        else:
            pygame.draw.circle(screen, BUTTON_COLOR, ((BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2), y), 10)
            #pygame.draw.rect(screen, BUTTON_COLOR, butoon)

    
    def drew_number(self, dis):
        y = ( SCREEN_HEIGHT - (self.num_floor+1)*FLOOR_HEIGHT + ((FLOOR_HEIGHT+BUTTOM_SPACE)/2))
        number = str(self.num_floor)
        font = pygame.font.SysFont('arial', FONT_SIZE)
        text = font.render(number, True, (0, 0, 255), None)
        text_react = text.get_rect()
        text_react.center = (BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2, y)
        dis.blit(text, text_react)

    def draw_timer(self, dis):
        y = (SCREEN_HEIGHT - (self.num_floor+1)*FLOOR_HEIGHT + ((FLOOR_HEIGHT+BUTTOM_SPACE)/2))
        time_remaining = self.timer.time_remaining()
        if time_remaining > 0:
            timer_str = f'{time_remaining:.2f}'
            font = pygame.font.Font('arial.ttf', FONT_SIZE)
            text = font.render(timer_str, True, (0, 0, 255), (255, 255, 255))
            text_react = text.get_rect()
            text_react.bottomleft = (BUILDING_POSITION_WIDTH + 4, y + FONT_SIZE/2)
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
    

    def play_sound(self):
        pygame.mixer.Sound('ding.mp3').play()





