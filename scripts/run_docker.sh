#!/bin/bash

docker build -t pygame-image .
xhost +
docker run -it --rm --name pygame-container -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix pygame-image

