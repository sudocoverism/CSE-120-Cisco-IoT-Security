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
    print('Finished Downloading')

def installDependencies():
    getDependencies()
    os.path.join('./scripts')
    subprocess.run('.\scripts\dependencyInstall.sh', shell=True)
