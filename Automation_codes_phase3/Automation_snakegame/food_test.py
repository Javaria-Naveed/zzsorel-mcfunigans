import unittest
from turtle import Turtle
from food import Food


class FoodTest(unittest.TestCase):

    def test_refresh(self):
        # Create a Food object
        food = Food()

        # Get the initial position of the food
        initial_x = food.xcor()
        initial_y = food.ycor()

        # Refresh the food's position
        food.refresh()

        # Get the new position of the food
        new_x = food.xcor()
        new_y = food.ycor()

        # Check if the food's position has changed
        self.assertNotEqual(initial_x, new_x)
        self.assertNotEqual(initial_y, new_y)


if __name__ == '__main__':
    unittest.main()
