from config import *
import pygame
from floor_class import *
from elevator_class import *
import math

class Building:

    def __init__(self):
        self.floors = [floor(i) for i in range(NUMBER_FLOORS)]
        self.elevators = [elevator(i) for i in range(NUMBER_ELEVATORS)]


    def draw_building(self, screen):
        for f in self.floors:
            f.draw_floor(screen)
            f.draw_button(screen)


    def conversion_button(self, x, y):
        if BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) < x < BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - (BUTTON_WIDTH//2) + BUTTON_WIDTH:
            return ((math.ceil(y/FLOOR_HEIGHT)) - 1)
        

    def order_elevator(self,floor):
        pass

