import pygame
import time
import math

# User input
NUMBER_FLOORS = 20
NUMBER_ELEVATORS = 1

# Window size
SCREEN_WIDTH =  1200
SCREEN_HEIGHT = 800
FILL_COLOR = (255,255,255)  # RGB

# World_size 
WORLD_WIDTH = SCREEN_WIDTH
WORLD_HEIGHT = NUMBER_FLOORS * 50

# Margin between the building and the edge of the window.
BUILDING_SIDE_MARGIN = SCREEN_WIDTH / 100 * 4 # 4 percent of the width of the window
BUILDING_TOP_MARGIN = 50    # in pixels

# Floor variables.
FLOOR_HEIGHT = 50 # (SCREEN_HEIGHT - BUILDING_TOP_MARGIN) // NUMBER_FLOORS
FLOOR_WIDTH = 100   # in pixels
TIME_PASS_FLOOR = 0.5   # in seconds
TIME_STOP_FLOOR = 2 # in seconds
LINE_WIDTH = 7  # in pixels
LINE_COLOR = (0, 0, 0)  # RGB
MID_LINE = LINE_WIDTH / 2 
TIMER_MARGIN = 4    # in pixels
TIMER_BACKGROUND = (255, 255, 255)  # RGB
FONT_SIZE = 12
FONT_COLOR = (0, 0, 0)  # RGB

# Button variables.
BUTTON_WIDTH = FLOOR_WIDTH / 4
BUTTON_HEIGHT = BUTTON_WIDTH #(FLOOR_HEIGHT + 20) // 2
BUTTON_COLOR = (255, 0, 0)  # RGB
BUTTON_PRESSED_COLOR = (0, 255, 0)  # RGB
CIRCLE_RADIUS = 10
BUTTOM_SPACE = 7
BORDER_RADIUS = 13

# Elevator variables.
ELEVATOR_H = FLOOR_HEIGHT - BUTTOM_SPACE
ELEVATOR_W = ELEVATOR_H


SCROLL_X = 0
SCROLL_Y = WORLD_HEIGHT - SCREEN_HEIGHT
SCROLL_SPEED = 10   # Pixels per key press

# File variables.
FONT = "assets/arial.ttf"
BACKGROUND_IMG = "assets/background.jpg"
ELEVATOR_IMG = "assets/elv.png"
FLOOR_IMG = "assets/bricks.jpg"
ELEVATOR_ARRIVAL_SOUND = "assets/ding.mp3"