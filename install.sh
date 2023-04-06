#!/bin/sh

git clone https://github.com/mikelogaciuk/deepscalecli.git
cd ./deepscalecli || exit
pip install poetry && poetry init && poetry shell
poetry install
curl https://github.com/Saafke/EDSR_Tensorflow/blob/master/models/EDSR_x2.pb
curl https://github.com/Saafke/EDSR_Tensorflow/blob/master/models/EDSR_x3.pb
curl https://github.com/Saafke/EDSR_Tensorflow/blob/master/models/EDSR_x4.pb
cp ESDR_x2.pb ./models/
cp ESDR_x3.pb ./models/
cp ESDR_x4.pb ./models/
