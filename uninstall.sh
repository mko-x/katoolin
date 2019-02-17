#!/bin/bash

echo "uninstall:start"

if [ "$EUID" -ne 0 ]
  then echo "uninstall: Please run as root"
  exit
fi

echo "uninstall:rm katoolin" 
rm -f /usr/bin/katoolin

echo "uninstall:autoremove"
apt-get -qq --purge autoremove -y

echo "uninstall:finish"
