#!/usr/bin/env bash

rm -rf tmp
rm setup.cfg

# install modules to temporary dir
mkdir tmp
pip install httplib2 -t ./tmp
pip install jsonpickle -t ./tmp
pip install oauth2client -t ./tmp
pip install google-api-python-client -t ./tmp
pip install datetime -t ./tmp
pip install lxml -t ./tmp

# required for aws lambda deployment package
echo '[install]' >> setup.cfg
echo 'prefix=' >> setup.cfg

# bundle everything
cd tmp && zip -r ../bundle.zip * && cd .. 
zip -r bundle.zip setup.cfg
zip -r bundle.zip *.py
zip -r bundle.zip credentials.json

# clean up
rm -rf tmp
rm setup.cfg
