import unittest
from unittest.mock import patch
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from turtle import Screen
import time

class GameIntegrationTest(unittest.TestCase):
    @patch('turtle.Turtle')
    @patch('time.sleep')
    @patch('turtle.Screen')
    def test_game_loop(self, mock_screen_class, mock_sleep, mock_turtle_class):
        screen_mock = mock_screen_class.return_value
        turtle_mock = mock_turtle_class.return_value

        # Create instances of Snake, Food, and ScoreBoard
        snake = Snake()
        food = Food()
        scoreboard = ScoreBoard()

        # Patch the onkey method to avoid actual screen listening
        screen_mock.onkey = lambda func, key: None

        # Run the game loop for a few iterations
        for _ in range(3):
            # Refresh the food and extend the snake
            snake.head.distance.return_value = 10
            food.refresh.return_value = None
            snake.extend.return_value = None
            scoreboard.increase_score.return_value = None

            # Move the snake
            snake.move.return_value = None

            # Check if snake head hits the wall
            snake.head.xcor.side_effect = [295, -301, 0]
            snake.head.ycor.side_effect = [0, 0, 301]

            # Reset the scoreboard and snake
            scoreboard.reset.return_value = None
            snake.reset.return_value = None

            # Check if snake head hits itself
            snake.head.distance.side_effect = [0, 20]

        # Run the game loop once more to trigger the exit condition
        screen_mock.update.return_value = None

        # Call the game loop
        with patch.object(time, 'sleep', side_effect=[0.1] * 6 + [None]):
            with patch('builtins.input', return_value=''):
                with self.assertRaises(SystemExit):
                    main_game_loop(screen_mock, snake, food, scoreboard)

        # Assertions for the method calls
        expected_calls = [
            mock_screen_class,
            mock_turtle_class,
            screen_mock.onkey,
            snake.head.distance,
            food.refresh,
            snake.extend,
            scoreboard.increase_score,
            snake.move,
            snake.head.xcor,
            snake.head.ycor,
            scoreboard.reset,
            snake.reset,
            snake.head.distance,
            screen_mock.update,
        ]
        mock_calls = mock_turtle_class.mock_calls + screen_mock.mock_calls
        self.assertEqual(mock_calls, expected_calls)

if __name__ == '__main__':
    unittest.main()
