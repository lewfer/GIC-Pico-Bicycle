# network.py
#
# Module that encapsulates wifi network functionality needed for robotics functions on a RPi Pico
# Uses UDP for sending and receiving messages
#
# https://learn.adafruit.com/pico-w-wifi-with-circuitpython/pico-w-basic-wifi-test


import wifi
import os
import socketpool
import ipaddress

class Network:
    def __init__(self, hostname=None):
        if hostname!=None:
            wifi.radio.hostname = hostname

    def connectWifi(self):
        #  Connect to your SSID
        wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

        print("Connected to WiFi...")

        self.host = wifi.radio.ipv4_address

        #  Prints MAC address 
        print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

        #  Prints IP address 
        print("My IP address is", self.host)

    # Remove contents from settings.toml to use this
    def startWifiAccessPoint(self, ap_ssid, ap_password):
        wifi.radio.hostname = "RPiPico"

        # Start access point
        wifi.radio.start_ap(ssid=ap_ssid, password=ap_password)

        
        self.host = wifi.radio.ipv4_address_ap

        # Show access point settings
        print("Access point created with SSID: {}, password: {}".format(ap_ssid, ap_password))

        #  Prints MAC address 
        print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

        # Show IP address
        print("IP address is", self.host)

    def createReceiver(self, port):
        # Create a socket pool to allow network comms
        pool = socketpool.SocketPool(wifi.radio)

        # Create socket bound to a port
        print("\nCreate UDP Server socket")
        self.socket = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
        self.socket.settimeout(None)
        self.socket.bind((str(self.host), port))

    def createSender(self, host, port):
        # Create a socket pool to allow network comms
        pool = socketpool.SocketPool(wifi.radio)

        # Create socket bound to a port
        print("\nCreate UDP Server socket")
        self.socket = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
        self.socket.settimeout(None)

        self.host = host
        self.port = port        

    def receiveMessage(self):
        MAXBUF = 256
        buf = bytearray(MAXBUF)
        size, addr = self.socket.recvfrom_into(buf)
        message = buf[:size].decode()
        return message
    
    def sendMessage(self, message):
        size = self.socket.sendto(str.encode(message), (self.host, self.port))
        return size

