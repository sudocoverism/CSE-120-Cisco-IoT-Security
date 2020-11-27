
function rootCheck {
  if [ $(id -u) != "0" ];
  then
    echo "You must be the superuser to run this script" >&2
    exit 1
  fi
}

function dependencyInstall {
  apt-get update

  dependencyName=(net-tools wireguard wireguard-tools original-awk libqrencode4 qrencode python3-pip qt5-default build-essential)

  for i in "${dependencyName[@]}"
    do
      echo "Installing $i"
      apt-get -y install $i
  done
}

function pythonDependencyInstall {
  apt-get update

  pythonDependencyName=(pyqt5)

  for i in "${pythonDependencyName[@]}"
    do
      echo "PIP Installing $i"
      pip3 install $i
  done
}


rootCheck
dependencyInstall
pythonDependencyInstall
exit
