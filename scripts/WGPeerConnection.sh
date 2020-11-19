#! /usr/bin/env bash
# linux command line script to install in the etc folder of the Server's root directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" ) >/")"

function addPeerPubKey {
  # echo the client's public key file into the server.conf
  # echo the client's IP address file into the server.conf
}

if [ -d "~/../etc/VPN" ]
then
 echo "VPN directory found."
 echo "Adding a device as a peer to the network"

else
 echo "VPN is not installed"
fi

exit
