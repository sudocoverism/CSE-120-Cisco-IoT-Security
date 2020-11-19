if#! /usr/bin/env bash
# linux command line script to install in the etc folder of the Server's root directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" ) >/")"

function keyGen {
 wg genkey | tee ~/../etc/VPN/privateKey | wg pubkey > ~/../etc/VPN/publicKey
 qrencode -l L -v 1 -o publicKey.png '
 $(cat ~/../etc/VPN/publicKey)
 '
 
}

function getIP {
 ifconfig | grep -A 1 "wlan0" | awk '{if(NR==2) print $2}' > ~/../etc/VPN/serverIPAddr
 qrencode cat ~/../etc/VPN/serverIPAddr
}

function serverConfig {
 echo "[Interface]" > ~/../etc/VPN/server.conf
 echo "PrivateKey=$(cat ~/../etc/VPN/privateKey)" >> ~/../etc/VPN/server.conf
 echo "Address=$(cat ~/../etc/VPN/serverIPAddr)/24" >> ~/../etc/VPN/server.conf
}

if [ ! -d "~/../home/VPN" ]
then
 echo "VPN directory does not exist."
 echo "Creating VPN directory"
 mkdir ~/../etc/VPN
 echo "Generating public and private keys"
 keyGen
 echo "Getting IP address of device"
 getIP
 echo "Configuring server"
 serverConfig
else
 echo "VPN directory already exists."
fi

exit
