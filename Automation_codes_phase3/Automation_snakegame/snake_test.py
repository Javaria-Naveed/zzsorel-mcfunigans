import unittest
from turtle import Turtle
from snake import Snake


class SnakeTest(unittest.TestCase):

    def setUp(self):
        self.snake = Snake()

    def test_initial_segments(self):
        self.assertEqual(len(self.snake.segments), 3)

    def test_move(self):
        initial_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake.move()
        new_positions = [(20, 0), (0, 0), (-20, 0)]
        for i in range(len(self.snake.segments)):
            self.assertEqual(self.snake.segments[i].position(), new_positions[i])

    def test_up(self):
        self.snake.up()
        self.assertEqual(self.snake.head.heading(), 90)

    def test_down(self):
        self.snake.down()
        self.assertEqual(self.snake.head.heading(), 270)

    def test_right(self):
        self.snake.right()
        self.assertEqual(self.snake.head.heading(), 0)

    def test_left(self):
        self.snake.left()
        self.assertEqual(self.snake.head.heading(), 180)

    def test_add_segment(self):
        initial_length = len(self.snake.segments)
        self.snake.add_segment((100, 100))
        self.assertEqual(len(self.snake.segments), initial_length + 1)

    def test_reset(self):
        self.snake.reset()
        self.assertEqual(len(self.snake.segments), 3)
        self.assertEqual(self.snake.head.heading(), 0)

    def test_extend(self):
        initial_length = len(self.snake.segments)
        self.snake.extend()
        self.assertEqual(len(self.snake.segments), initial_length + 1)

    def tearDown(self):
        self.snake = None


if __name__ == '__main__':
    unittest.main()
