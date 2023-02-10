# tic_tac_toe
This is a simple tic tac toe game.

Run the game with:

```sh
chmod +x run_docker.sh
./run_docker.sh
```

You can run the command xhost + on your host machine before running the container to allow the container to connect to the X server:

Run tests:

```sh
python3 -m unittest tests/test_TicTacToe.py
```