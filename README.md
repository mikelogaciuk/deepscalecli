# deepscalecli

## About

Simple CLI built with `Typer` and `OpenCV` used to up-scale old family photos with deep learning using ESDR models ([link](https://github.com/Saafke/EDSR_Tensorflow/tree/master/models)).

## Install

`Python 3.10` and `Poetry` are needed in order to use it.

Process to directory that you wish to install it and type:

```shell
git clone https://github.com/mikelogaciuk/deepscalecli.git 
cd deepscalecli || exit
chmod +x ./install.sh
./install.sh
```

## Usage

To scale photography, use:

```shell
$ deepscalecli scale X
```

Where X is the size of up-scaling size.

Only 2, 3 and 4 are currently available. 

## Clean up

In order to cleanup results folder, please type:

```shell
$ deepscalecli cleanup
```