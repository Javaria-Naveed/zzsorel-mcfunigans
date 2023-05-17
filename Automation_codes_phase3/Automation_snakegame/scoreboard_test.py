import unittest
from unittest.mock import patch
from turtle import Turtle
from scoreboard import ScoreBoard


class ScoreBoardTest(unittest.TestCase):

    def setUp(self):
        self.score_board = ScoreBoard()

    def test_initial_score_and_high_score(self):
        self.assertEqual(self.score_board.score, 0)
        self.assertEqual(self.score_board.high_score, 9)

    def test_increase_score(self):
        initial_score = self.score_board.score
        self.score_board.increase_score()
        self.assertEqual(self.score_board.score, initial_score + 1)

    def test_reset_score(self):
        self.score_board.score = 5
        self.score_board.high_score = 10
        self.score_board.reset()
        self.assertEqual(self.score_board.score, 0)
        self.assertEqual(self.score_board.high_score, 10)

    def tearDown(self):
        self.score_board = None


if __name__ == '__main__':
    unittest.main()
