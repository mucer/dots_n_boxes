# Bibliotheken laden
from machine import Pin, Timer
from neopixel import NeoPixel
from time import sleep_ms
#from webserver import Webserver
import webserver2
import _thread

### Dani lib
from lib.cell_pos import CellPos

MATRIX_SIZE = 15

class Player:
    pos_x = -1
    pos_y = -1
    player_id = -1
    direction = "up"
    
    def __init__(self, x, y, player_id):
        self.x = x
        self.y = y
        self.player_id = player_id
        
    def move(self):
        if self.direction == "left": self.x -= 1
        elif self.direction == "right": self.x += 1
        elif self.direction == "up": self.y += 1
        elif self.direction == "down": self.y -= 1
        
        if self.x >= (MATRIX_SIZE) or self.x < 0 or self.y < 0 or self.y >= (MATRIX_SIZE):
            #self.x, self.y = 0, 0
            #self.direction = "up"
            raise ValueError('player went out of matrix')
            
    def moveLeft(self):
        self.direction = "left"
        
    def moveRight(self):
        self.direction = "right"
        
    def moveUp(self):
        self.direction = "up"
        
    def moveDown(self):
        self.direction = "down"
        
        
class DisplayController:
    
    def __init__(self, size: int):

        self.MATRIX_SIZE = size

        self.pixels_left_front = NeoPixel(Pin(29, Pin.OUT), self.MATRIX_SIZE * self.MATRIX_SIZE * 2)
        self.pixels_top_right = NeoPixel(Pin(28, Pin.OUT), self.MATRIX_SIZE * self.MATRIX_SIZE * 2)
    
    def updateMatrix(self):
        self.pixels_left_front.write()
        self.pixels_top_right.write()
    
    def writePixel(self, cell: CellPos):
        
        if(cell.side.size != self.MATRIX_SIZE)

        brightness = 10
        color = (brightness, brightness, brightness)

        x = cell.x
        y = cell.y
        side = cell.name

        if x >= self.MATRIX_SIZE or x < 0:
            return False
        if y >= self.MATRIX_SIZE or y < 0:
            return False

        i = 0  # strip index
        max_val = self.MATRIX_SIZE * self.MATRIX_SIZE * 2

        # --- first Strip
        if side == "front":
            if y % 2 == 0:  # ->
                i = x + (y * self.MATRIX_SIZE) + (self.MATRIX_SIZE * (y + 1))
            else:  # <-
                i = (y * self.MATRIX_SIZE) + (self.MATRIX_SIZE * (y + 1)) - 1 - x
        elif side == "left":
            if y % 2 == 0:  # ->
                i = x + (y * self.MATRIX_SIZE * 2)
            else:  # <-
                i = (self.MATRIX_SIZE - x - 1) + (y * (self.MATRIX_SIZE * 2) + X)

        # --- second Strip
        elif side == "top":
            if y % 2 == 0:  # <-
                i = max_val - (x + (self.MATRIX_SIZE * y * 2) + 1)
            else:  # ->
                i = max_val - ((self.MATRIX_SIZE - x - 1) + (y * (self.MATRIX_SIZE * 2) + self.MATRIX_SIZE) + 1)

        elif side == "right":

            zero = max_val - self.MATRIX_SIZE * 2

            if x % 2 == 0:  # 1
                            # |
                i = (zero - x * self.MATRIX_SIZE * 2) + y

            else:  # |
                   # y
                i = (zero - (x - 1) * self.MATRIX_SIZE * 2) - 1 - y  # -1 to get offest

        if side == "left" or side == "front":
            self.pixels_left_front[i] = color
            return True
        if side == "top" or side == "right":
            self.pixels_top_right[i] = color
            return True
        
    def fullColor(self, r, g, b):
        self.clearMatrix()
        self.updateMatrix()
        for i in range(0, MATRIX_SIZE * MATRIX_SIZE * 2): self.pixels_left_front[i] = (r, g, b)
        for i in range(0, MATRIX_SIZE * MATRIX_SIZE * 2): self.pixels_top_right[i] = (r, g, b)
        self.updateMatrix()
        sleep_ms(500)
        self.clearMatrix()
        self.updateMatrix()
        
    def clearMatrix(self):
        self.pixels_left_front.fill((0,0,0))
        self.pixels_top_right.fill((0,0,0))

        
class GameLogic:
    players = [
        #Player(0, 0, 1),
        Player(0, 0, 2)
    ]
    display_controller = DisplayController()
    
    def movePlayers(self):
        for player in self.players:
            player.move()
        
    def writePlayerPosToMatrix(self):
        for player in self.players:
            self.display_controller.writePixel(player.x, player.y)
            
    def tick(self, timer):
        self.display_controller.clearMatrix()
        try:
            self.movePlayers()
        except ValueError:
            self.gameOver(timer)
        self.writePlayerPosToMatrix()
        self.display_controller.updateMatrix()
        
    def gameOver(self, timer):
        timer.deinit()
        self.display_controller.fullColor(255, 0, 0)
        sleep_ms(500)
        self.display_controller.fullColor(255, 0, 0)
        sleep_ms(500)
        self.display_controller.fullColor(255, 0, 0)
        
        # restart the game
        self.players = [Player(0, 0, 2)]
        timer.init(period=1000, mode=Timer.PERIODIC, callback=gamelogic.tick)

gamelogic = GameLogic()

speed = 500

#webserver = Webserver()


def my_function(self):
    gamelogic.tick()
# Create a Timer object
timer = Timer(-1)
# Set the interval to 1000 milliseconds (1 second)
timer.init(period=speed, mode=Timer.PERIODIC, callback=gamelogic.tick)

while True:
    #gamelogic.tick()
    #sleep_ms(speed)
    #webserver.tick()
    webserver2.webserver_hook(gamelogic)
    pass