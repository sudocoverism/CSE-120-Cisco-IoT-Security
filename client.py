import subprocess
import os
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.lang import builder


#RPI display is 320x480p
#Window.size = (320, 480)

qrcode: ObjectProperty(Label())


class MainScreen(Screen):
    pass

class ZBarCamScreen(Screen):
    pass

class P(FloatLayout):
    def dupekey(self, pubkey):
        popup = Popup(title='Error',
                      content=Label(text='Duplicate Public Key: '.join(pubkey)),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

    def dupeip(self, ipaddr):
        popup = Popup(title='Error',
                      content=Label(text='Duplicate IP Address: '.join(ipaddr)),
                      size_hint=(None, None), size=(400, 400))
        popup.open()
    pass

class ClientApp(App):
    def remove(self, key):
        print("Work in progress")

    def save(self, key):
        trimmedkey = key[2:-1]
        #file = os.path.dirname('tempclient.txt')
        keys = trimmedkey.split('\\n')
        pubkey = key[2:-18]
        ipaddr = key[48:-3]
        keytype = [pubkey, ipaddr]
        keylist = open(os.path.join('ClientInfo' , 'client.conf'), 'r')
        f = open(os.path.join('ClientInfo', 'tempclient.txt'), 'w')
        f.write('\nPublicKey=')
        f.write(keys[0])
        f.write('\nEndpoint=')
        f.write(keys[1])
        #only difference between client and server main.py
        f.write('/24:51820')
        f.close()
        subprocess.run('./scripts/clientAddPeerConfig.sh', shell=True)

    #
    def setup(self):
        subprocess.run('./scripts/clientInterfaceConfig.sh', shell=True)

    def power(self, switchobject, switchvalue):
        if (switchvalue):
            os.system("wg-quick up ./ClientInfo/client.conf")
        else:
            os.system("wg-quick down ./ClientInfo/client.conf")

    pass


if __name__ == '__main__':
    ClientApp().run()
