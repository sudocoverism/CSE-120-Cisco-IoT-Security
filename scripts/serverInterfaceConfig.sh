#! /usr/bin/env bash
# linux command line script to install in the etc folder of the Server's root directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" ) >/")"

function keyGen {
 wg genkey | tee ServerInfo/privateKey | wg pubkey > ServerInfo/publicKey
 #cat ~/../etc/VPN/publicKey | qrencode -l L -v 1 -o ~/../etc/VPN/publicKey.png ''
}

function getIP {
 ifconfig | grep -A 1 "wlan0\|etho0\|wlp61s0" | awk '{if(NR==2) print $2}' > ServerInfo/serverIPAddr
 #cat ~/../etc/VPN/serverIPAddr | qrencode -l L -v 1 -o ~/../etc/VPN/ipAddrKey.png ''
}

function serverConfig {
 echo "[Interface]" > ServerInfo/server.conf
 echo "PrivateKey=$(cat ServerInfo/privateKey)" >> ServerInfo/server.conf
 echo "Address=$(cat ServerInfo/serverIPAddr)/24" >> ServerInfo/server.conf
 echo "ListenPort=51820" >> ServerInfo/server.conf
 echo "PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -A FORWARD -o %i -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE" >> ServerInfo/server.conf
 echo "PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -D FORWARD -o %i -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE" >> ServerInfo/server.conf
 cat ServerInfo/publicKey ServerInfo/serverIPAddr > ServerInfo/key
 cat ServerInfo/key | qrencode -l L -v 1 -o ServerInfo/keys.png
}

echo "Creating VPN directory"
mkdir ServerInfo database
echo "Generating public and private keys"
keyGen
echo "Getting IP address of device"
getIP
echo "Configuring server"
serverConfig

exit
