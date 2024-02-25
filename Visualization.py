from neopixel import NeoPixel
from machine import Pin, Timer
#from enum import Enum

class Side:
    FRONT = 1
    LEFT = 2
    TOP = 3
    RIGHT = 4


class Visualization:

    MATRIX_SIZE = 15

    def __init__(self):
    
        self.pixels_left_front = NeoPixel(Pin(29, Pin.OUT), self.MATRIX_SIZE * self.MATRIX_SIZE * 2)
        self.pixels_top_right = NeoPixel(Pin(28, Pin.OUT), self.MATRIX_SIZE * self.MATRIX_SIZE * 2)

    def draw_pixel(self, side, x, y, color):
        # todo remove
        self.pixels_left_front.fill((0,0,0))
        self.pixels_top_right.fill((0,0,0))

        if x >= self.MATRIX_SIZE or x < 0:
            return False
        if y >= self.MATRIX_SIZE or y < 0:
            return False

        i = 0  # strip index
        max_val = self.MATRIX_SIZE * self.MATRIX_SIZE * 2

        # --- first Strip
        if side == Side.FRONT:
            if y % 2 == 0:  # ->
                i = x + (y * self.MATRIX_SIZE) + (self.MATRIX_SIZE * (y + 1))
            else:  # <-
                i = (y * self.MATRIX_SIZE) + (self.MATRIX_SIZE * (y + 1)) - 1 - x
        elif side == Side.LEFT:
            if y % 2 == 0:  # ->
                i = x + (y * self.MATRIX_SIZE * 2)
            else:  # <-
                i = (self.MATRIX_SIZE - x - 1) + (y * (self.MATRIX_SIZE * 2) + X)

        # --- second Strip
        elif side == Side.TOP:
            if y % 2 == 0:  # <-
                i = max_val - (x + (self.MATRIX_SIZE * y * 2) + 1)
            else:  # ->
                i = max_val - ((self.MATRIX_SIZE - x - 1) + (y * (self.MATRIX_SIZE * 2) + self.MATRIX_SIZE) + 1)

        elif side == Side.RIGHT:
            # TODO: Handle RIGHT side
            pass

        if side == Side.LEFT or side == Side.FRONT:
            self.pixels_left_front[i] = color
            # todo remove
            self.pixels_left_front.write()
            self.pixels_top_right.write()
            return True
        if side == Side.TOP or side == Side.RIGHT:
            self.pixels_top_right[i] = color
            # todo remove
            self.pixels_left_front.write()
            self.pixels_top_right.write()
            return True
        print(i)
        return False


