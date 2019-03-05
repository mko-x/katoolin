#!/bin/bash
set -ex

BUILD_FOLDER_PATH="./build"

if [ -e "$BUILD_FOLDER_PATH" ]; then
    rm -Rf $BUILD_FOLDER_PATH
fi

mkdir $BUILD_FOLDER_PATH

cp -Rf app $BUILD_FOLDER_PATH/app
cp -Rf tmpl $BUILD_FOLDER_PATH/tmpl
cp -f __init__.py $BUILD_FOLDER_PATH
cp -f install.sh $BUILD_FOLDER_PATH
cp -f uninstall.sh $BUILD_FOLDER_PATH
cp -f katoolin.py $BUILD_FOLDER_PATH
cp -f LICENCE $BUILD_FOLDER_PATH
cp -f README.md $BUILD_FOLDER_PATH

