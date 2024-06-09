from config import *
from Timer import *

class Floor:
    def __init__(self, floor_num):
        """
        Initializes a Floor object.

        Args:
        - floor_num (int): The floor number.

        Attributes:
        - timer (Timer): A Timer object representing the time until the elevator arrives at the floor.
        - timer_closing (Timer): A Timer object representing the time until the elevator door closes.
        - num_floor (int): The floor number.
        - floor_available (bool): Indicates whether the floor is available for an elevator to pick up.
        """
        self.timer = Timer(0)  # Timer for elevator arrival time
        self.timer_closing = Timer(0)  # Timer for door closing time
        self.num_floor = floor_num  # Floor number
        self.floor_available = True  # Flag indicating if the floor is available
        self.butoon = None # Represents the button object
        # Variables containing the x and y coordinates of the button
        self.y_button = SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT + (FLOOR_HEIGHT + BUTTOM_SPACE) / 2
        self.x_button = BUILDING_SIDE_MARGIN + FLOOR_WIDTH / 2


    def draw_floor(self, screen):
        """
        Draws the floor on the screen.

        Args:
            screen (pygame.Surface): Pygame display surface.
        """
        # Calculate the y-coordinate of the floor and Blit the floor image onto the screen
        y = (SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT)
        image = pygame.image.load(FLOOR_IMG).convert()
        screen.blit(image, (BUILDING_SIDE_MARGIN, y), (0, 0, FLOOR_WIDTH, FLOOR_HEIGHT))
        # Draw a line to represent the separation between floors
        pygame.draw.line(screen, LINE_COLOR, (BUILDING_SIDE_MARGIN, y + MID_LINE),
                         (BUILDING_SIDE_MARGIN + FLOOR_WIDTH - 1, y + MID_LINE), LINE_WIDTH)


    def draw_button(self, screen):
        """
        Draws the button on the screen.

        Args:
            screen (pygame.Surface): Pygame display surface.
        """
        y = self.y_button
        x = self.x_button
        self.butoon = pygame.Rect(x - (BUTTON_WIDTH/2), y - (BUTTON_WIDTH/2), BUTTON_WIDTH, BUTTON_HEIGHT)
        if self.timer_closing.time_remaining() > 0:
            pygame.draw.rect(screen, (255, 0, 0), self.butoon, 0, BORDER_RADIUS)
        else:
            pygame.draw.rect(screen, (0, 255, 0), self.butoon, 0, BORDER_RADIUS)


    def button_pressed(self, x, y):
        """
        Checks if the button on this floor has been pressed.

        Args:
        - x (int): x-coordinate of the place of the click.
        - y (int): y-coordinate of the place of the click.

        Returns:
        - int or None: Floor number if the button was pressed, None otherwise.
        """
        if self.butoon.collidepoint(x, y):
            return self.num_floor


    def drew_number(self, screen):
        """
        Draws the floor number on the screen.

        Args:
            dis (pygame.Surface): Pygame display surface.
        """
        # Display the floor number text with the font, color, and background color
        number = str(self.num_floor)
        font = pygame.font.Font(FONT, FONT_SIZE)
        text = font.render(number, True, FONT_COLOR, None)
        text_react = text.get_rect()
        text_react.center = (self.x_button, self.y_button)
        screen.blit(text, text_react)


    def draw_timer(self, dis):
        """
        Draws the timer indicating when an elevator arrives.
        
        Args:
            dis: Pygame display.
        """
        # Display the timer text with the font, color, and background color
        time_remaining = self.timer.time_remaining()
        if time_remaining > 0:
            timer_str = f'{time_remaining:.2f}'
            font = pygame.font.Font(FONT, FONT_SIZE)
            text = font.render(timer_str, True, FONT_COLOR, TIMER_BACKGROUND)
            text_react = text.get_rect()
            text_react.bottomleft = (BUILDING_SIDE_MARGIN + TIMER_MARGIN, self.y_button + FONT_SIZE / 2)
            dis.blit(text, text_react)


    def elevator_arrive(self, time):
        """
        Handles elevator arrival at the floor.

        Args:
        - time (float): Time until the elevator arrives at the floor.
        """
        self.timer = Timer(time)  # Set timer for elevator arrival
        self.timer_closing = Timer(time + TIME_STOP_FLOOR)  # Set timer for door closing

    def draw_building(self, screen):
        """
        Draws the entire floor layout on the screen.

        Args:
        - screen (pygame.Surface): Pygame display surface.
        """
        self.draw_floor(screen)
        self.draw_button(screen)
        self.drew_number(screen)
        self.draw_timer(screen)


    def update_floor_availability(self):
        """
        Updates the availability of the floor for an elevator pickup.

        Returns:
        - bool: True if the floor is available, False otherwise.
        """
        if self.timer_closing.time_remaining() > 0:
            self.floor_available = False
        else:
            self.floor_available = True
        return self.floor_available


    def play_sound(self):
        """Plays the elevator arrival sound."""
        pygame.mixer.Sound(ELEVATOR_ARRIVAL_SOUND).play()
