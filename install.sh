#!/bin/bash

echo "install:start"

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

export PYTHON_DOWNLOAD_VERSION="2.7.15-8"
export PYTHON_PACKAGE_VERSION="2.7"
export PYTHON_VERSION_TARGET="Python 2.7.15+"
export PYTHON="/usr/bin/python${PYTHON_PACKAGE_VERSION}"

echo "install:platform detection"

platform='unknown'
unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
   platform='linux'
elif [[ "$unamestr" == 'darwin' ]]; then
   platform='osx'
fi

export OS_PLATFORM="${platform}"
echo "install:platform detected=${OS_PLATFORM}"

echo "install:python version detection"
installed_python_version="python --version"
if [[ "$installed_python_version" == ${PYTHON_VERSION_TARGET} ]]; then
   export PYTHON_VERSION_TARGET_INSTALLED=${PYTHON_VERSION_TARGET}
else
    apt-get install "python${PYTHON_PACKAGE_VERSION}"
fi

PYTHON_OK=`$PYTHON -c 'import sys
print (sys.version_info >= (2, 7) and "1" or "0")'`
echo "python ok status value: ${PYTHON_OK}"

if [ "$platform" = 'Linux' ]; then
    PYTHON_OK='99'
fi

if [ "$PYTHON_OK" = '0' ]; then
    echo "install:python version too old"
    echo "install:python building from source"
    echo "install.python.building:apt update"
    apt-get -qq update -y
    echo "install.python.building:apt install essentials"
    apt-get -qq install -y build-essential checkinstall
    echo "install.python.building:apt install dev libs"
    apt-get -qq install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

    echo "install.python.building:get python release "
    cd /usr/src && wget https://www.python.org/ftp/python/${PYTHON_DOWNLOAD_VERSION}/Python-${PYTHON_DOWNLOAD_VERSION}.tgz && tar xzf Python-${PYTHON_DOWNLOAD_VERSION}.tgz
    cd Python-${PYTHON_DOWNLOAD_VERSION}
    ./configure --enable-optimizations
    make altinstall
else
    apt-get update -y
    apt-get install -y python${PYTHON_PACKAGE_VERSION}
fi

apt-get -qq --purge autoremove -y

echo "Python install ensured"

rm -f /usr/bin/katoolin
cp ./katoolin.py /usr/bin/katoolin
chmod +x /usr/bin/katoolin

echo "Fin"
echo "Run katoolin just from terminal e.g. by calling katoolin"
