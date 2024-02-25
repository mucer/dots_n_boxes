# Bibliotheken laden
import socket
import time
import network
#from test import GameLogic

# HTML
#html = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="shortcut icon" href="data:"><title>Raspberry Pi Pico</title></head><body><h1 align="center">Raspberry Pi Pico W</h1><p align="center">Verbindung mit %s</p></body></html>"""
html = """
        <!DOCTYPE html>
<html>
<head>
    <title>Pico Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        .arrow-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px; /* Höhe des Steuerkreuzes */
        }
        .arrow {
            font-size: 48px;
            width: 60px;
            height: 60px;
            border: none;
            background: none;
            cursor: pointer;
            color: #007bff; /* Standardfarbe für die Pfeiltasten */
            transition: color 0.3s; /* Animationsübergang */
        }
        .arrow:hover {
            color: #0056b3; /* Farbe bei Hover */
        }
    </style>
</head>
<body>
    <h1>Raspberry Pi Pico Web Server</h1>
    <h2>Snake</h2>
    <div class="arrow-container">
        <form action="./up">
            <button class="arrow" type="submit">&uarr;</button> <!-- Pfeil nach oben -->
        </form>
    </div>
    <div class="arrow-container">
        <form action="./left">
            <button class="arrow" type="submit">&larr;</button> <!-- Pfeil nach links -->
        </form>
        <form action="./right">
            <button class="arrow" type="submit">&rarr;</button> <!-- Pfeil nach rechts -->
        </form>
    </div>
    <div class="arrow-container">
        <form action="./down">
            <button class="arrow" type="submit">&darr;</button> <!-- Pfeil nach unten -->
        </form>
    </div>
</body>
</html>

"""

ap = network.WLAN(network.AP_IF)
ap.config(essid="Pi_Pico_Snake", password="HackenMitLicht")
ap.active(True)

while ap.active() == False:
    pass
print('AP Mode Is Active, You can Now Connect')
print('IP Address To Connect to:: ' + ap.ifconfig()[0])


print('Starting server')
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(addr)
server.listen(1)
print('Server is listening on', addr)
print()

# Auf eingehende Verbindungen hören
def webserver_hook(gamelogic):
    conn, addr = server.accept()
    print('HTTP-Request from client', addr)
    request = conn.recv(1024)
    # HTTP-Request anzeigen
    print('Request:', request)
    
    request = str(request)
    print('Request content = %s' % request)

    try:
        request = request.split()[1]
        #print('Request:', request)
    except IndexError:
        pass
    
    # Process the request and update variables
    if request == '/right?':
        gamelogic.players[0].moveRight()
    elif request == '/left?':
        gamelogic.players[0].moveLeft()
    elif request == '/up?':
        gamelogic.players[0].moveUp()
    elif request == '/down?':
        gamelogic.players[0].moveDown()

    
    # HTTP-Response senden
    #response = html % str(addr)
    response = html
    conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    conn.send(response)
    conn.close()
    print('HTTP-Response gesendet')
    print()


#while True:
#    tick()
