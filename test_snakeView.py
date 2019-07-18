import unittest
from snakeView import SnakeView

class TestSnakeView(unittest.TestCase):
    
    def test_printSnake(self):
        view = SnakeView()
        self.assertRaises(TypeError, view.printSnake, [[None, None],[None],None])
        self.assertRaises(TypeError, view.printSnake, [[None, 500],[500, 500-1],[500, 500-2]])
        self.assertRaises(TypeError, view.printSnake, [[500, None],[500, 500-1],[500, 500-2]])
        self.assertRaises(ValueError, view.printSnake, [[500],[500],[500]])
        self.assertRaises(ValueError, view.printSnake, [[500, 500-1],[500, None], [500, 500-2]])
        self.assertRaises(ValueError, view.printSnake, [[500]])

    def test_printFood(self):
        pass
    
    def test_printSnakeTail(self):
        pass
        
