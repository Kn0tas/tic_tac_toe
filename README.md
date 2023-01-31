# tic_tac_toe
This is a simple tic tac toe game.

Build the container from the same location as the Dockerfile with:

```sh
docker build -t pygame-image .
```

You can run the command xhost + on your host machine before running the container to allow the container to connect to the X server:

```sh
xhost +
docker run -it --rm --name pygame-container -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix pygame-image
```

Run tests

```sh
python3 -m unittest tests/test_TicTacToe.py
```