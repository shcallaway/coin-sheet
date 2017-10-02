#!/usr/bin/env bash

rm -rf lib
rm setup.cfg

# install modules to temporary dir
mkdir lib
pip install httplib2 \
            jsonpickle \
            oauth2client \
            google-api-python-client \
            datetime \
            lxml \
            -t ./lib

# create setup.cfg
echo '[install]' >> setup.cfg
echo 'prefix=' >> setup.cfg

# zip modules
cd lib
zip -r ../bundle.zip *
cd .. 

# zip everything else
zip -r bundle.zip setup.cfg
zip -r bundle.zip *.py
zip -r bundle.zip credentials.json

# clean up
rm -rf lib
rm setup.cfg
