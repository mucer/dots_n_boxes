from neopixel import NeoPixel
from enum import Enum

class Side(Enum):
    FRONT = 1
    LEFT = 2
    TOP = 3
    RIGHT = 4


class Visualization:

    MATRIX_SIZE = 16

    def __init__():
    
        pixels_left_front = NeoPixel(Pin(28, Pin.OUT), MATRIX_SIZE * MATRIX_SIZE)
        pixels_top_right = NeoPixel(Pin(29, Pin.OUT), MATRIX_SIZE * MATRIX_SIZE)

    def draw_pixel(side, x, y, color):
        if x >= X or x < 0:
            return False
        if y >= Y or y < 0:
            return False

        i = 0  # strip index
        max_val = X * Y * 2

        # --- first Strip
        if side == Side.FRONT:
            if y % 2 == 0:  # ->
                i = x + (y * X) + (X * (y + 1))
            else:  # <-
                i = (y * X) + (X * (y + 1)) - 1 - x
        elif side == Side.LEFT:
            if y % 2 == 0:  # ->
                i = x + (y * X * 2)
            else:  # <-
                i = (X - x - 1) + (y * (X * 2) + X)

        # --- second Strip
        elif side == Side.TOP:
            if y % 2 == 0:  # <-
                i = max_val - (x + (X * y * 2) + 1)
            else:  # ->
                i = max_val - ((X - x - 1) + (y * (X * 2) + X) + 1)

        elif side == Side.RIGHT:
            # TODO: Handle RIGHT side
            pass

        if side == Side.LEFT or side == Side.FRONT:
            self.pixels_left_front[i] = color
            return True
        if side == Side.TOP or side == Side.RIGHT:
            self.pixels_top_right[i] = color
            return True
        print(i)
        return False


