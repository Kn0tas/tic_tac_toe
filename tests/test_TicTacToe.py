import sys
sys.path.append("..")
from main import TicTacToe
import unittest
from tests.test_TicTacToe import *

class TestTicTacToe(unittest.TestCase):
    def test_initial_board(self):
        game = TicTacToe()
        self.assertEqual(game.board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "Expected empty board")

    def test_horizontal_win(self):
        game = TicTacToe()
        game.board = [[1, 1, 1],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.assertTrue(game.check_winner(), "Expected horizontal win")
        
    def test_vertical_win(self):
        game = TicTacToe()
        game.board = [[1, 0, 0],
                      [1, 0, 0],
                      [1, 0, 0]]
        self.assertTrue(game.check_winner(), "Expected vertical win")
        
    def test_diagonal_win(self):
        game = TicTacToe()
        game.board = [[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]]
        self.assertTrue(game.check_winner(), "Expected diagonal win")

if __name__ == '__main__':
    unittest.main()