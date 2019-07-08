import unittest
from snakeModel import SnakeModel

class TestSnakeModel(unittest.TestCase):
    
    def testClassInit(self):
        self.assertRaises(ValueError, SnakeModel, -2, -2)
        self.assertRaises(ValueError, SnakeModel, -2, 500)
        self.assertRaises(ValueError, SnakeModel, 500, -2)
        self.assertRaises(ValueError, SnakeModel, 0, 0)
        self.assertRaises(TypeError, SnakeModel, .2, .2)
        self.assertRaises(TypeError, SnakeModel, "hello", -2J)
    
    def testHeadInsert(self):
        snake = SnakeModel(500, 500)
        oneElemHead = [1]
        ThreeElemhead = [1,1,1]
        self.assertRaises(TypeError, snake.insertSnakeHead)
        self.assertRaises(ValueError, snake.insertSnakeHead, oneElemHead)
        self.assertRaises(ValueError, snake.insertSnakeHead, ThreeElemhead)