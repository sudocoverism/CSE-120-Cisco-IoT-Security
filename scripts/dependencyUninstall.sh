
function rootCheck {
  if [ $(id -u) != "0" ];
  then
    echo "You must be the superuser to run this script" >&2
    exit 1
  fi
}

function dependencyInsttall {
  apt-get update

  dependencyName= (net-tools wireguard wireguard-tools original-awk libqrencode4 qrencode qt5-default pyqt5 build-essential)


  for i in "${dependencyName[@]}"
    do
      echo "Removing $i"
      apt remove -y $i
  done
}


rootCheck
dependencyInsttall
exit
