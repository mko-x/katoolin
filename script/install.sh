#!/bin/bash

echo "install:start"

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

export PYTHON_DOWNLOAD_VERSION="2.7.15-8"
export PYTHON_PACKAGE_VERSION="2.7"
export PYTHON_VERSION_MINIMUM="279"
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
echo "install:platform '${OS_PLATFORM}'' detected"

echo "install:python version detection"

version=$($PYTHON -V 2>&1 | grep -Po '(?<=Python )(.+)')
if [[ -z "$version" ]]
then
    echo "install:no python!" 
fi
prepareParsedVersion=$(echo "${version//./}")
parsedVersion=$(echo "${prepareParsedVersion//rc1/}")
if [[ "$parsedVersion" -gt "$PYTHON_VERSION_MINIMUM" ]]
then 
    echo "install:valid version '${parsedVersion}' found"
    export PYTHON_VERSION_TARGET_INSTALLED=${PYTHON_VERSION_TARGET}
else
    echo "install:invalid/outdated version '${parsedVersion}' found"
    echo "install:installation of required python binaries"
    apt-get install -qq -y "python${PYTHON_PACKAGE_VERSION}"
fi

PYTHON_OK=`$PYTHON -c 'import sys
print (sys.version_info >= (2, 7) and "1" or "0")'`
echo "install:python ok status value: ${PYTHON_OK}"

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
fi

if [ ! -f "$PYTHON" ]; then
    echo "install:not found '$PYTHON'"
    echo "install:updating apt-get"
    apt-get update -y -qq
    echo "install:install python binaries"
    apt-get install -qq -y python${PYTHON_PACKAGE_VERSION}
fi

echo "install:clean apt-get"
apt-get -qq --purge autoremove -y

echo "Python install ensured"

echo "Installation of katoolin started..."
echo "Removing old stuff"
rm -rf /usr/bin/katoolin
rm -rf /usr/bin/katlib

echo "Copying new stuff"
cp ../src/katoolin.py /usr/bin/katoolin
cp -R ../src/katlib /usr/bin/katlib

echo "Fit permissions"
chmod +x /usr/bin/katoolin
chmod -R +x /usr/bin/katlib

echo "... Installation of katoolin finished!"
echo "Run katoolin just from the commandline e.g. by calling 'sudo katoolin'"
