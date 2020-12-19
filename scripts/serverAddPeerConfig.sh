#! /usr/bin/env bash
# linux command line script to install in the etc folder of the Server's root directory

function addPeer {
  # echo the client's public key file into the server.conf
  # echo the client's IP address file into the server.conf
  #echo "\n" >> ServerInfo/server.conf
  printf "\n[Peer]" >> ServerInfo/server.conf
  cat ServerInfo/tempclient.txt >> ServerInfo/server.conf
}

if [ -f "ServerInfo/server.conf" ]
then
 echo "VPN directory found."
 echo "Adding a device as a peer to the network"
 addPeer
else
 echo "VPN is not installed"
fi

exit
