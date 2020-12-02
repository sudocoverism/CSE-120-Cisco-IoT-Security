import os
import requests
import subprocess
import urllib.request as urllib

def getDependencies(url = 'https://drive.google.com/uc?export=download&id=1l9AMbUfJn7RuX3P_0MMxeeHA9G3iJwbK', filename=''):
    folder = os.path.exists('./scripts')
    if folder:
        pass
    else:
        os.mkdir('scripts')

    print('Downloading Required Files')
    filename = 'dependencyInstall.sh'
    filepath = os.path.join('./scripts', filename)
    urllib.urlretrieve('https://drive.google.com/uc?export=download&id=1l9AMbUfJn7RuX3P_0MMxeeHA9G3iJwbK', filepath)
    filename = 'dependencyUninstall.sh'
    filepath = os.path.join('./scripts', filename)
    urllib.urlretrieve('https://drive.google.com/uc?export=download&id=1kNVrMK2UdWAi-eMdZpLqNi6PglcjWTUr', filepath)
    filename = 'ipQRCode.sh'
    filepath = os.path.join('./scripts', filename)
    urllib.urlretrieve('https://drive.google.com/uc?export=download&id=1IPpMy5ptlpkpRGW8dorVQ-oUJuZrB9Es', filepath)
    filename = 'publicKeyQRCode.sh'
    filepath = os.path.join('./scripts', filename)
    urllib.urlretrieve('https://drive.google.com/uc?export=download&id=12JkJQTZJILfdHG10bdhlEVvBOex4wuUw', filepath)
    filename = 'wgInterfaceConfig.sh'
    filepath = os.path.join('./scripts', filename)
    urllib.urlretrieve('https://drive.google.com/uc?export=download&id=159pOfS93tiRksBAb_7pAcGMTazMm8Cry', filepath)
    filename = 'wgPeerConnection.sh'
    filepath = os.path.join('./scripts', filename)
    urllib.urlretrieve('https://drive.google.com/uc?export=download&id=1x-tSWFdHkhM3SYHnjjHnaVejKpzrVWAV', filepath)

def installDependencies():
    getDependencies()
    os.path.join('./scripts')
    subprocess.run('.\scripts\dependencyInstall.sh', shell=True)
