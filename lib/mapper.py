class Mapper:
    def __init__(self, size):
        self.SIZE = size
        self.pixels_left_front = [(0, 0, 0)] * (self.SIZE * self.SIZE * 2)
        self.pixels_top_right = [(0, 0, 0)] * (self.SIZE * self.SIZE * 2)

    def pos_to_pixel(self, side, x, y):
        if x >= self.SIZE or x < 0 or y >= self.SIZE or y < 0:
            return [-1,0]

        i = 0  # strip index
        max_val = self.SIZE * self.SIZE * 2

        # --- first Strip
        if side == "front":
            if y % 2 == 0:  # ->
                i = x + (y * self.SIZE) + (self.SIZE * (y + 1))
            else:  # <-
                i = (y * self.SIZE) + (self.SIZE * (y + 1)) - 1 - x
        elif side == "left":
            if y % 2 == 0:  # ->
                i = x + (y * self.SIZE * 2)
            else:  # <-
                i = y * self.SIZE * 2 + self.SIZE * 2 - x - 1

        # --- second Strip
        elif side == "top":
            if y % 2 == 0:  # <-
                i = max_val - (x + (self.SIZE * y * 2) + 1)
            else:  # ->
                i = max_val - ((self.SIZE - x - 1) + (y * (self.SIZE * 2) + self.SIZE) + 1)

        elif side == "right":

            zero = max_val - self.SIZE * 2

            if x % 2 == 0:  # 1
                            # |
                i = (zero - x * self.SIZE * 2) + y

            else:  # |
                   # y
                i = (zero - (x - 1) * self.SIZE * 2) - 1 - y  # -1 to get offest

        print("--", side)
        if side == "left" or side == "front":
            return [0, i]
        if side == "top" or side == "right":
            return [1, i]
