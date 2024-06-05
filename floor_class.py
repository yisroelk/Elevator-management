from config import *
from timer_class import *


class Floor:

    def __init__(self, i):
        self.timer = Timer(0)   
        self.timer_color = Timer(0)          
        self.num_floor = i
        self.floor_available = True
        self.dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        

    def draw_floor(self, screen):
        y = (SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT)
        image = pygame.image.load(FLOOR_IMG).convert()
        screen.blit(image, (BUILDING_SIDE_MARGIN, y), (0, 0, FLOOR_WIDTH, FLOOR_HEIGHT))
        pygame.draw.line(screen, LINE_COLOR, (BUILDING_SIDE_MARGIN, y + MID_LINE), \
                         (BUILDING_SIDE_MARGIN + FLOOR_WIDTH - 1, y + MID_LINE), LINE_WIDTH)


    def draw_button(self, screen):
        y = (SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT + ((FLOOR_HEIGHT + BUTTOM_SPACE) / 2))
        if self.timer_color.time_remaining() > 0:
            pygame.draw.circle(screen, BUTTON_PRESSED_COLOR, ((BUILDING_SIDE_MARGIN + FLOOR_WIDTH // 2), y), CIRCLE_RADIUS)
        else:
            pygame.draw.circle(screen, BUTTON_COLOR, ((BUILDING_SIDE_MARGIN + FLOOR_WIDTH // 2), y), CIRCLE_RADIUS)

    
    def drew_number(self, dis):
        y = (SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT + ((FLOOR_HEIGHT+BUTTOM_SPACE) / 2))
        number = str(self.num_floor)
        font = pygame.font.Font(FONT, FONT_SIZE)
        text = font.render(number, True, FONT_COLOR, None)
        text_react = text.get_rect()
        text_react.center = (BUILDING_SIDE_MARGIN + FLOOR_WIDTH // 2, y)
        dis.blit(text, text_react)


    def draw_timer(self, dis):
        y = (SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT + ((FLOOR_HEIGHT + BUTTOM_SPACE) / 2))
        time_remaining = self.timer.time_remaining()
        if time_remaining > 0:
            timer_str = f'{time_remaining:.2f}'
            font = pygame.font.Font(FONT, FONT_SIZE)
            text = font.render(timer_str, True, FONT_COLOR, TIMER_BACKGROUND)
            text_react = text.get_rect()
            text_react.bottomleft = (BUILDING_SIDE_MARGIN + TIMER_MARGIN, y + FONT_SIZE / 2)
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
        pygame.mixer.Sound(ELEVATOR_ARRIVAL_SOUND).play()
