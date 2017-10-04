#!/usr/bin/env bash

CREDENTIALS=credentials.json
SETUP=setup.cfg
MODULES=./lib

rm -rf $MODULES
rm $SETUP

# install modules
mkdir lib
pip install httplib2 \
            jsonpickle \
            oauth2client \
            google-api-python-client \
            datetime \
            lxml \
            -t $MODULES

# create setup.cfg
echo '[install]' >> $SETUP
echo 'prefix=' >> $SETUP

# make sure permissions are good
chmod u=rw,g=r,o=r $CREDENTIALS

# zip everything
cd lib && zip -r ../bundle.zip * && cd .. 

zip -r bundle.zip $SETUP
zip -r bundle.zip *.py
zip -r bundle.zip $CREDENTIALS

# clean up
rm -rf lib
rm $SETUP
