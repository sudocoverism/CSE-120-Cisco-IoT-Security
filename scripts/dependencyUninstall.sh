
function rootCheck {
  if [ $(id -u) != "0" ];
  then
    echo "You must be the superuser to run this script" >&2
    exit 1
  fi
}

function dependencyUninstall {
  apt-get update

  dependencyName= (net-tools wireguard wireguard-tools original-awk libqrencode4 qrencode qt5-default build-essential)


  for i in "${dependencyName[@]}"
    do
      echo "Removing $i"
      apt remove -y $i
  done
}

function pythonDependencyUninstall {
  apt-get update

  pythonDependencyName=(pyqt5)

  for i in "${dependencyName[@]}"
    do
      echo "PIP Removing $i"
      pip3 uninstall $i
  done
}


rootCheck
dependencyUninstall
pythonDependencyUninstall
exit
