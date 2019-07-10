import unittest
from snakeModel import SnakeModel

class TestSnakeModel(unittest.TestCase):
    
    def test_SnakeModelInit(self):

        self.assertRaises(TypeError, SnakeModel)
        typerErrorscreenSizes = [
            {"screenHeight": .2, "screenWidth" : .2},
            {"screenHeight": 'hello', "screenWidth" : -2J},
            None
        ]
        for screensize in typerErrorscreenSizes:
             self.assertRaises(TypeError, SnakeModel, screensize)

        valueErrorScreenSizes =[
            {"screenHeight": -2, "screenWidth" : -2},
            {"screenHeight": -2, "screenWidth" : 500},
            {"screenHeight": 500, "screenWidth" : -2},
            {"screenHeight": 0, "screenWidth" : 0}
        ]      
        for screensize in valueErrorScreenSizes:
             self.assertRaises(ValueError, SnakeModel, screensize)
    
    def test_insertSnakeHead(self):
        snake = SnakeModel({"screenHeight": 500, "screenWidth" : 500})
        oneElemHead = [1]
        ThreeElemhead = [1,1,1]
        noIntHead = [1, "ciao"]
        self.assertRaises(TypeError, snake.insertSnakeHead)
        self.assertRaises(TypeError, snake.insertSnakeHead, noIntHead)
        self.assertRaises(ValueError, snake.insertSnakeHead, oneElemHead)
        self.assertRaises(ValueError, snake.insertSnakeHead, ThreeElemhead)