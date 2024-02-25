# Bibliotheken laden
from machine import Pin, Timer
from neopixel import NeoPixel
from time import sleep_ms
from Visualization import Visualization, Side
#from webserver import Webserver
import webserver2
import _thread

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
    #pixels = NeoPixel(Pin(28, Pin.OUT), MATRIX_SIZE * MATRIX_SIZE)
    
    def __init__(self, visualization: Visualization):

        self.visualization = visualization

    def updateMatrix(self):
        #self.pixels.write()
        pass
    
    def writePixel(self, x: int, y: int):
        
        brightness = 10
        c = (brightness, brightness, brightness)
        self.visualization.draw_pixel(Side.TOP, x, y, c)
        
    def fullColor(self, r, g, b):
        self.clearMatrix()
        self.updateMatrix()
        for i in range(0, MATRIX_SIZE * MATRIX_SIZE): self.pixels[i] = (r, g, b)
        self.updateMatrix()
        sleep_ms(500)
        self.clearMatrix()
        self.updateMatrix()
        
    def clearMatrix(self):
        #self.pixels.fill((0,0,0))
        pass
        
class GameLogic:
    players = [
        #Player(0, 0, 1),
        Player(0, 0, 2)
    ]
    display_controller = DisplayController(Visualization())
    
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
    
