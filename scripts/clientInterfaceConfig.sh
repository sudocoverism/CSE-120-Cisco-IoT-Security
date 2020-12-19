#! /usr/bin/env bash
# linux command line script to install in the etc folder of the client's root directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" ) >/")"

function keyGen {
 wg genkey | tee ClientInfo/privateKey | wg pubkey > ClientInfo/publicKey
 #cat ~/../etc/VPN/publicKey | qrencode -l L -v 1 -o ~/../etc/VPN/publicKey.png ''
}

function getIP {
 ifconfig | grep -A 1 "wlan0\|etho0\|wlp*" | awk '{if(NR==2) print $2}' > ClientInfo/clientIPAddr
 #cat ~/../etc/VPN/clientIPAddr | qrencode -l L -v 1 -o ~/../etc/VPN/ipAddrKey.png ''
}

function clientConfig {
 echo "[Interface]" > ClientInfo/client.conf
 echo "PrivateKey=$(cat ClientInfo/privateKey)" >> ClientInfo/client.conf
 echo "Address=$(cat ClientInfo/clientIPAddr)" >> ClientInfo/client.conf
 echo "ListenPort=51820" >> ClientInfo/client.conf
 cat ClientInfo/publicKey ClientInfo/clientIPAddr > ClientInfo/key
 cat ClientInfo/key | qrencode -l L -v 1 -o ClientInfo/keys.png
}

echo "VPN directory does not exist."
echo "Creating VPN directory"
mkdir ClientInfo
echo "Generating public and private keys"
keyGen
echo "Getting IP address of device"
getIP
echo "Configuring client"
clientConfig

exit
