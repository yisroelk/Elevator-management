import pygame
import time
import math



SCREEN_WIDTH =  700
SCREEN_HEIGHT = 700

NUMBER_FLOORS = 20
NUMBER_ELEVATORS = 3

FLOOR_HEIGHT = SCREEN_HEIGHT//NUMBER_FLOORS #(96*SCREEN_HEIGHT)//100//NUMBER_FLOORS
FLOOR_WIDTH = 100

BUTTON_WIDTH = FLOOR_WIDTH//4
BUTTON_HEIGHT = (68*FLOOR_HEIGHT)//100
BUTTON_SPACE = 7

ELEVATOR_H = FLOOR_HEIGHT - BUTTON_SPACE
ELEVATOR_W = ELEVATOR_H

BUILDING_POSITION_WIDTH = SCREEN_WIDTH//100*10
BUILDING_POSITION_HEIGHT = 0 #SCREEN_HEIGHT//100*2



TIME_PASS_FLOOR = 0.5
TIME_STOP_FLOOR = 2

print(FLOOR_HEIGHT,BUTTON_HEIGHT, BUTTON_WIDTH)