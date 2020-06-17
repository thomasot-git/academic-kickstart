#!/bin/sh

echo "Installing dependencies"
pip3 install -U git+https://github.com/OrganicIrradiation/scholarly.git

echo "Extracting Scholar data"
python bin/generatescholar.py

echo "Saving Scholar json on data folder"
# mkdir -p data
# mv citecount.json data/

echo "Calling hugo"
hugo
