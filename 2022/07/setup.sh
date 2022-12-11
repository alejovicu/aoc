#!/usr/bin/env bash

rm -rf .env

virtualenv --python=/usr/bin/python3 .env

source .env/bin/activate

pip3 install -r requirements.txt