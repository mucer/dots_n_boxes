import network
import time
import socket


class Webserver:
    def __init__(self):
        self.ap_mode('Pi_Pico_Snake', 'HackenMitLicht')
        self.s = None
    
    def web_page(self):
      html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
                <body><h1>Hello World</h1></body></html>
             """
      return html

    # if you do not see the network you may have to power cycle
    # unplug your pico w for 10 seconds and plug it in again
    def ap_mode(self, ssid, password):
        """
            Description: This is a function to activate AP mode
            
            Parameters:
            
            ssid[str]: The name of your internet connection
            password[str]: Password for your internet connection
            
            Returns: Nada
        """
        # Just making our internet connection
        ap = network.WLAN(network.AP_IF)
        ap.config(essid=ssid, password=password)
        ap.active(True)
        
        while ap.active() == False:
            pass
        print('AP Mode Is Active, You can Now Connect')
        print('IP Address To Connect to:: ' + ap.ifconfig()[0])
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
        self.s.bind(('', 80))
        self.s.listen(5)

    def tick(self):
        if self.s == None:
            #print("return")
            return
        conn, addr = self.s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        print('Content = %s' % str(request))
        response = self.web_page()
        conn.send(response)
        conn.close()
        
webserver = Webserver()
while True:
    webserver.tick()

