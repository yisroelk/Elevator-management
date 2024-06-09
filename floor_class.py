from config import *
from timer_class import *

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
        self.butoon = None
        self.y_button = SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT + (FLOOR_HEIGHT + BUTTOM_SPACE) / 2
        self.x_button = BUILDING_SIDE_MARGIN + FLOOR_WIDTH // 2

    def draw_floor(self, screen):
        """
        Draws the floor on the screen.

        Args:
            screen (pygame.Surface): Pygame display surface.
        """
        # Calculate the y-coordinate of the floor
        y = (SCREEN_HEIGHT - (self.num_floor + 1) * FLOOR_HEIGHT)
        # Load the floor image
        image = pygame.image.load(FLOOR_IMG).convert()
        # Blit the floor image onto the screen
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
        self.butoon = pygame.Rect(x - (BUTTON_WIDTH//2), y - (BUTTON_WIDTH//2), BUTTON_WIDTH, BUTTON_HEIGHT - 5)
        if self.timer_closing.time_remaining() > 0:
            pygame.draw.rect(screen, (255, 0, 0), self.butoon, 0, 10)
        else:
            pygame.draw.rect(screen, (0, 255, 0), self.butoon, 0, 10)


    def button_pressed(self, x, y):
        if self.butoon.collidepoint(x, y):
            return self.num_floor


    def drew_number(self, screen):
        """
        Draws the floor number on the screen.

        Args:
            dis (pygame.Surface): Pygame display surface.
        """
        # Convert the floor number to a string
        number = str(self.num_floor)
        # Create a font object with the specified font and size
        font = pygame.font.Font(FONT, FONT_SIZE)
        # Render the floor number text with the font, color, and background color
        text = font.render(number, True, FONT_COLOR, None)
        # Get the rectangle bounding the text
        text_react = text.get_rect()
        # Center the text on the floor
        text_react.center = (self.x_button, self.y_button)
        # Blit the text onto the display surface
        screen.blit(text, text_react)

    def draw_timer(self, dis):
        """
        Draws the timer indicating when an elevator arrives.
        
        Args:
            dis: Pygame display.
        """
        # Get the remaining time from the timer
        time_remaining = self.timer.time_remaining()
        if time_remaining > 0:
            # Format the time string with two decimal places
            timer_str = f'{time_remaining:.2f}'
            # Create a font object with the specified font and size
            font = pygame.font.Font(FONT, FONT_SIZE)
            # Render the timer text with the font, color, and background color
            text = font.render(timer_str, True, FONT_COLOR, TIMER_BACKGROUND)
            # Get the rectangle bounding the text
            text_react = text.get_rect()
            # Position the bottom left corner of the text rectangle
            text_react.bottomleft = (BUILDING_SIDE_MARGIN + TIMER_MARGIN, self.y_button + FONT_SIZE / 2)
            # Blit the text onto the display
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
            self.floor_available = False  # Set floor availability to False if timer is running
        else:
            self.floor_available = True  # Set floor availability to True if timer is not running
        return self.floor_available  # Return floor availability status

    def play_sound(self):
        """Plays the elevator arrival sound."""
        pygame.mixer.Sound(ELEVATOR_ARRIVAL_SOUND).play()
