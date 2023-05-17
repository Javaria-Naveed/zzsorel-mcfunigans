import copy
import numpy as np

goalMap = dict(
    {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 0})
goalState = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])


def check(s, visited):
    for v in visited:
        if s.state == v.state:
            return True
    return False


def PrintState(state):
    for i in range(0, 3):
        print(state[i])


class State:
    def __init__(self):
        self.state = np.array()
        self.actualCost = 0
        self.parent = State()

    def __init__(self, state, actualCost):
        self.state = state
        self.actualCost = actualCost


# Calculates heuristic value for a state
def getHeuristicCost(state):
    hCost = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] != goalMap[(i, j)]:
                hCost = hCost + 1
    return hCost


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if (getHeuristicCost(self.queue[i].state) + self.queue[i].actualCost) < (
                        getHeuristicCost(self.queue[min].state) + self.queue[min].actualCost):
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()


class Puzzle:
    def __init__(self):
        self.heuristicCost = 0
        self.state = State(np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)
        self.stateMoves = {(0, 0): [(0, 1), (1, 0)],
                           (0, 1): [(0, 0), (1, 1), (0, 2)],
                           (0, 2): [(0, 1), (1, 2)],
                           (1, 0): [(0, 0), (1, 1), (2, 0)],
                           (1, 1): [(0, 1), (1, 0), (1, 2), (2, 1)],
                           (1, 2): [(0, 2), (1, 1), (2, 2)],
                           (2, 0): [(1, 0), (2, 1)],
                           (2, 1): [(2, 0), (1, 1), (2, 2)],
                           (2, 2): [(1, 2), (2, 1)]
                           }

    def __init__(self, puzzle):
        self.state = puzzle
        self.goalState = State(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), 0)
        self.stateMoves = {(0, 0): [(0, 1), (1, 0)],
                           (0, 1): [(0, 0), (1, 1), (0, 2)],
                           (0, 2): [(0, 1), (1, 2)],
                           (1, 0): [(0, 0), (1, 1), (2, 0)],
                           (1, 1): [(0, 1), (1, 0), (1, 2), (2, 1)],
                           (1, 2): [(0, 2), (1, 1), (2, 2)],
                           (2, 0): [(1, 0), (2, 1)],
                           (2, 1): [(2, 0), (1, 1), (2, 2)],
                           (2, 2): [(1, 2), (2, 1)]
                           }

    def setState(self):
        for i in range(0, 3):
            for j in range(0, 3):
                val = input('Enter value for index ' + str(i) + ',' + str(j) + ' : ')
                self.state[i][j] = val

    def emptySpaceLoc(self, state):
        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == 0:
                    return (i, j)

    def move(self, state):
        newState = copy.deepcopy(state)
        emptyLoc = self.emptySpaceLoc(newState.state)
        moves = self.stateMoves[emptyLoc]
        states = []
        for m in moves:
            s = copy.deepcopy(newState)
            s.state[emptyLoc[0]][emptyLoc[1]] = s.state[m[0]][m[1]]
            s.state[m[0]][m[1]] = 0
            s.parent = newState
            s.actualCost = s.actualCost + 1
            states.append(s)
        return states

    def solvePuzzle(self):
        q = PriorityQueue()
        q.insert(self.state)
        path = [self.state.state]
        visited = [self.state]
        solved = False
        goal = None
        while not q.isEmpty() and not solved:
            s = q.delete()
            if np.array_equal(s.state, goalState):
                print('Puzzle Solved !')
                goal = s
                solved = True
            states = self.move(s)
            for s in states:
                if check(s, visited) == False:
                    q.insert(s)
                    visited.append(s)
        path = []
        while goal.parent is not None:
            path.append(goal)
            goal = goal.parent
        path.reverse()
        print('Total Steps : ' + str(len(path)))
        print('Steps')
        for p in path:
            PrintState(p.state)
            print('---------')


# Modify the below matrix to change the input for the Puzzle Solver !
s = State([[2, 8, 3]
              , [1, 6, 4],
           [7, 0, 5]],
          0)

s.parent = None
p = Puzzle(s)
p.solvePuzzle()
