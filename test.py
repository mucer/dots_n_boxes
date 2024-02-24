# Bibliotheken laden
from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

MATRIX_SIZE = 16

class Player:
    pos_x = -1
    pos_y = -1
    player_id = -1
    
    def __init__(self, x, y, player_id):
        self.x = x
        self.y = y
        self.player_id = player_id
        
    def move(self):
        self.x += 1
        self.y += 1
        
        if self.x >= (MATRIX_SIZE - 1) or self.y >= (MATRIX_SIZE - 1):
            self.x, self.y = 0, 0
        
class DisplayController:
    pixels = NeoPixel(Pin(28, Pin.OUT), MATRIX_SIZE * MATRIX_SIZE)
    
    def updateMatrix(self):
        self.pixels.write()
    
    def writePixel(self, x: int, y: int):
        pixelIndex = -1
        if y % 2 == 0: # on odd rows
            pixelIndex = x + (y * MATRIX_SIZE);
        else:
          pixelIndex = (MATRIX_SIZE - x - 1) + (y * MATRIX_SIZE);
        
        brightness = 10
        self.pixels[pixelIndex] = (brightness, brightness, brightness)
        
    def clearMatrix(self):
        self.pixels.fill((0,0,0))
        
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
            
    def tick(self):
        self.display_controller.clearMatrix()
        self.movePlayers()
        self.writePlayerPosToMatrix()
        self.display_controller.updateMatrix()

gamelogic = GameLogic()

speed = 500


while True:
    gamelogic.tick()
    sleep_ms(speed)
    
