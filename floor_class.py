from config import *
import pygame

class floor:

    def __init__(self, i):
        self.timer = 0              # "return to here"
        self.num_floor = i
        # background
        

    def draw_floor(self, screen):
        y = (self.num_floor*FLOOR_HEIGHT) # ""FIX THE POSITION!!""
        floor = pygame.Rect((BUILDING_POSITION_WIDTH, y, FLOOR_WIDTH, FLOOR_HEIGHT))
        pygame.draw.rect(screen, (0,187,255), floor)
        pygame.draw.line(screen,(0,0,0),(BUILDING_POSITION_WIDTH, y + FLOOR_HEIGHT - 7),(BUILDING_POSITION_WIDTH + FLOOR_WIDTH-1,y + FLOOR_HEIGHT - 7),7)


    def draw_button(self, screen):
        y = (self.num_floor*FLOOR_HEIGHT) + 2 # ""FIX THE POSITION!!""
        butoon = pygame.Rect((BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) , y, BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(screen, (0,255,0), butoon)

    
    def number(self):
        
        



