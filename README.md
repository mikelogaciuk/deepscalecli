# deepscalecli

## About

Simple image scaller, used to scale Dalle-E images from [OpenAI's DALL-E](https://openai.com/blog/dall-e/).

## Installation

```bash
mkdirp -p ~/repos && cd ~/repos 
git clone https://github.com/mikelogaciuk/deepscalecli.git & cd deepscalecli
```

```bash
poetry shell && poetry install
```

## Usage

```bash
# Scale all images from ~/Downloads/ to 4x using FSRCNN Model and save them to ~/Dalle
deepscalecli scale fsrcnn 4 ~/Downloads/ ~/Dalle   
```

## Code

This is as simple as it could be. 

One function for scaling, one decorator for time measurement and one function for CLI.

## Models

All respective rights for models belong to their respective owners.
