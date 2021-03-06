#!/bin/bash
set -ex

BUILD_FOLDER_BASE_PATH="../build"

if [ -e "$BUILD_FOLDER_BASE_PATH" ]; then
    rm -Rf $BUILD_FOLDER_BASE_PATH
fi

mkdir -p $BUILD_FOLDER_BASE_PATH

cp -Rf katlib $BUILD_FOLDER_BASE_PATH/katlib
cp -Rf tmpl $BUILD_FOLDER_BASE_PATH/tmpl
cp -f __init__.py $BUILD_FOLDER_BASE_PATH
cp -f install.sh $BUILD_FOLDER_BASE_PATH
cp -f uninstall.sh $BUILD_FOLDER_BASE_PATH
cp -f katoolin.py $BUILD_FOLDER_BASE_PATH
cp -f LICENCE $BUILD_FOLDER_BASE_PATH
cp -f README.md $BUILD_FOLDER_BASE_PATH