import os
import time

# Assuming we have a GUI or something, we can use this script to automate the QR code display and connection process

# Assuming that the path of the script is in the same directory as this python script
PATH = ''

os.system('sudo bash {}publicKeyQRcode.sh'.format(PATH))
os.system('sudo bash {}WGPeerConnection.sh'.format(PATH))
