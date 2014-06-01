#!/usr/bin/env bash

cd /vagrant
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt