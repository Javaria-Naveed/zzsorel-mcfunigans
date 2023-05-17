import copy
import numpy as np
import pytest
import main
import unittest

# Test getHeuristicCost function
def test_getHeuristicCost():
    state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    assert main.getHeuristicCost(state) == 0

    state = np.array([[1, 2, 0], [8, 4, 3], [7, 6, 5]])
    assert main.getHeuristicCost(state) == 2

    state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    assert main.getHeuristicCost(state) == 8


# Test Puzzle class methods
def test_Puzzle_methods():
    puzzle = main.Puzzle()
    puzzle.setState()

    # Test emptySpaceLoc method
    state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    assert puzzle.emptySpaceLoc(state) == (1, 1)

    state = np.array([[1, 2, 3], [8, 4, 0], [7, 6, 5]])
    assert puzzle.emptySpaceLoc(state) == (1, 2)

    # Test move method
    state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    moves = puzzle.move(state)
    assert len(moves) == 2


# Test PriorityQueue class
def test_PriorityQueue():
    pq = main.PriorityQueue()
    state1 = main.State(np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]]), 0)
    state2 = main.State(np.array([[1, 2, 0], [8, 4, 3], [7, 6, 5]]), 2)
    state3 = main.State(np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]]), 8)

    pq.insert(state1)
    pq.insert(state2)
    pq.insert(state3)

    assert pq.delete() == state2
    assert pq.delete() == state1
    assert pq.delete() == state3


# Test check function
def test_check():
    state1 = main.State(np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]]), 0)
    state2 = main.State(np.array([[1, 2, 0], [8, 4, 3], [7, 6, 5]]), 2)
    state3 = main.State(np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]]), 8)

    visited = [state1, state2]

    assert main.check(state1, visited) == True
    assert main.check(state2, visited) == True
    assert main.check(state3, visited) == False


# Test solvePuzzle method
def test_solvePuzzle():
    s = main.State(np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]]), 0)
    p = main.Puzzle(s)

    # Test solving the puzzle
    p.solvePuzzle()


# Run the test functions
if __name__ == "__main__":
    test_getHeuristicCost()
    test_Puzzle_methods()
    test_PriorityQueue()
    test_check()
    test_solvePuzzle()

