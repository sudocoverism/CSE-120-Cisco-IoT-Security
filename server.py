import subprocess
import os
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup


#RPI display is 320x480p
#Window.size = (320, 480)

qrcode: ObjectProperty(Label())


class MainScreen(Screen):
    pass

class ZBarCamScreen(Screen):
    pass

class ZBarCamScreen2(Screen):
    pass

class P(FloatLayout):
    pass

class ServerApp(App):
    def remove(self, key):
        print("Work in progress")

    def save(self, key):
        trimmedkey = key[2:-1]
        #file = os.path.dirname('tempclient.txt')
        keys = trimmedkey.split('\\n')
        pubkey = key[2:-18]
        ipaddr = key[48:-3]
        keytype = [pubkey, ipaddr]
        keylist = open(os.path.join('ServerInfo' , 'server.conf'), 'r')
        f = open(os.path.join('ServerInfo', 'tempclient.txt'), 'w')
        f.write('\nPublicKey=')
        f.write(keys[0])
        f.write('\nAllowedIPs=')
        f.write(keys[1])
        f.write('/32')
        f.close()
        subprocess.run('./scripts/serverAddPeerConfig.sh', shell=True)
    def setup(self):
        subprocess.run('./scripts/serverInterfaceConfig.sh', shell=True)
    def power(self, switchobject, switchvalue):
        if (switchvalue):
            os.system("wg-quick up ./ServerInfo/server.conf")
        else:
            os.system("wg-quick down ./ServerInfo/server.conf")
    pass

if __name__ == '__main__':
    ServerApp().run()
