#!/usr/bin/env bash

#Tested on an unstable Raspberry Pi OS with Wireguard and awk installed
#command to run is 'bash server.sh'

#linux command line script
function keyGen {
 wg genkey | tee /home/$USER/VPN/privateKey | wg pubkey > /home/$USER/VPN/publicKey
}

function getIP {
 ifconfig | grep -A 1 "wlan0" | awk '{if(NR==2) print $2}' > /home/$USER/VPN/serverIPAddr
}

function serverConfig {
 echo "[Interface]" > /home/$USER/VPN/server.conf
 echo "PrivateKey=$(cat /home/$USER/VPN/privateKey)" >> /home/$USER/VPN/server.conf
 echo "Address=$(cat /home/$USER/VPN/serverIPAddr)/24" >> /home/$USER/VPN/server.conf
}

if [ ! -d "/home/$USER/VPN" ]
then
 echo "VPN directory does not exist."
 echo "Creating VPN directory"
 mkdir VPN
 echo "Generating public and private keys"
 keyGen
 echo "Getting IP address of device"
 getIP
 echo "Configuring server"
 serverConfig
else
 echo "VPN directory already exists."
fi
