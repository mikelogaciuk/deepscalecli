#!/bin/sh

pip install poetry && poetry init && poetry shell
poetry install
mkdir -p models && mkdir -p results
curl https://github.com/Saafke/EDSR_Tensorflow/blob/master/models/EDSR_x2.pb --output ./models/EDSR_x2.pb
curl https://github.com/Saafke/EDSR_Tensorflow/blob/master/models/EDSR_x3.pb --output ./models/EDSR_x3.pb
curl https://github.com/Saafke/EDSR_Tensorflow/blob/master/models/EDSR_x4.pb --output ./models/EDSR_x4.pb
