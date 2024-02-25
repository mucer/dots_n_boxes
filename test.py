# Bibliotheken laden
from machine import Pin, Timer
from neopixel import NeoPixel
from time import sleep_ms
#from webserver import Webserver
import webserver2
from random import randrange
from lib.cell_pos import CellPos
from lib.side import Side
from lib.enums import Direction

MATRIX_SIZE = 16
speed = 500

class Player:
    
    def __init__(self, pos, direction, player_id):
        self.pos = pos
        self.player_id = player_id
        self.direction = direction
        self.body = []
        self.previous_pos = self.pos
        
    def move(self):
        self.previous_pos = self.pos.clone()
        d = -1
        if self.direction == "left": d = Direction.LEFT
        elif self.direction == "right": d = Direction.RIGHT
        elif self.direction == "up": d = Direction.UP
        elif self.direction == "down": d = Direction.DOWN
        
        
        if not self.pos.move(d):
            raise ValueError('player went out of matrix')
            
    def moveLeft(self):
        print("left")
        self.direction = "left"
        
    def moveRight(self):
        self.direction = "right"
        
    def moveUp(self):
        self.direction = "up"
        
    def moveDown(self):
        self.direction = "down"
        
    def moveBody(self):
        if len(self.body) > 0:
            self.body.insert(0, self.previous_pos)
            self.body.pop()
        for b in self.body:
            if self.pos.x == b.x and self.pos.y == b.y: raise ValueError('player bite itself')
        
    def addLength(self):
        
        print(self.previous_pos == self.pos)
        if len(self.body) == 0:
            self.body.append(self.previous_pos)
        else:
            self.body.append(self.body[-1])
        
    def getSnakePixels(self):
        pass
        
        
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
        
    def fullColor(self, r, g, b):
        self.clearMatrix()
        self.updateMatrix()
        for i in range(0, MATRIX_SIZE * MATRIX_SIZE): self.pixels[i] = (r, g, b)
        self.updateMatrix()
        sleep_ms(500)
        self.clearMatrix()
        self.updateMatrix()
        
    def clearMatrix(self):
        self.pixels.fill((0,0,0))
        
class GameLogic:
    front = Side("front", MATRIX_SIZE)
    players = [
        #Player(0, 0, 1),
        Player(CellPos(front, 0, 0), "up", 2)
    ]
    cookies = []#[(0,1),(0,2),(0,3),(0,4),(0,5)]
    display_controller = DisplayController()
    
    def __init__(self):
        self.generateCookies()
    
    def checkCookies(self):
        for cookie in self.cookies:
            for player in self.players:
                pass
                if cookie.x == player.pos.x and cookie.y == player.pos.y:
                    self.display_controller.fullColor(0, 22, 0)
                    player.addLength()
                    self.cookies.remove(cookie)
        self.generateCookies()
                    
    def generateCookies(self):
        while len(self.cookies) < 2:
            self.cookies.append(CellPos(self.front, randrange(MATRIX_SIZE-1),randrange(MATRIX_SIZE-1)))
    
    def movePlayers(self):
        for player in self.players:
            player.move()
            self.checkCookies()
            player.moveBody()
        
    def writePlayerPosToMatrix(self):
        for player in self.players:
            self.display_controller.writePixel(player.pos.x, player.pos.y)
            for b in player.body:
                self.display_controller.writePixel(b.x, b.y)
            
    def writeCookiesToMatrix(self):
        for cookie in self.cookies:
            self.display_controller.writePixel(cookie.x, cookie.y)
            
    def tick(self, timer):
        self.display_controller.clearMatrix()
        try:
            self.movePlayers()
        except ValueError:
            self.gameOver(timer)
        self.writePlayerPosToMatrix()
        self.writeCookiesToMatrix()
        self.display_controller.updateMatrix()
        
    def gameOver(self, timer):
        timer.deinit()
        self.display_controller.fullColor(255, 0, 0)
        sleep_ms(500)
        self.display_controller.fullColor(255, 0, 0)
        sleep_ms(500)
        self.display_controller.fullColor(255, 0, 0)
        
        # restart the game
        self.players = [Player(CellPos(self.front, 0, 0), "up", 2)]
        #self.cookies = [(0,1),(0,2),(0,3),(0,4),(0,5)]
        timer.init(period=speed, mode=Timer.PERIODIC, callback=gamelogic.tick)

gamelogic = GameLogic()

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
    
