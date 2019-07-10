import random
import curses

class SnakeView:
    
    def __init__(self):
        self.REFRESH_RATE = 100
        self.screen = curses.initscr()
        self.screenHeight, self.screenWidth = self.screen.getmaxyx()
        curses.curs_set(0) # No cursor in the screen
        self.gameWindow = curses.newwin(self.screenHeight, self.screenWidth, 0, 0)
        self.gameWindow.keypad(1)
        self.gameWindow.timeout(self.REFRESH_RATE)

    def getWindowChar(self):
        return self.gameWindow.getch()
    
    def printSnake(self, snake):
        if not isinstance(snake, list):
            raise TypeError
        if len(snake) < 1 or len(snake[0]) < 2:
            raise ValueError
        if not isinstance(snake[0][1], int) or not isinstance(snake[0][0], int):
            raise TypeError
        if snake[0][1] >= self.screenWidth or snake[0][0] >= self.screenHeight:
            raise ValueError
        try:
            self.gameWindow.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
        except Exception:
            self.destroyWindow()
            raise curses.error
        
    def printFood(self, food):
        self.gameWindow.addch(food[0], food[1], curses.ACS_PI)

    def printSnakeTail(self, tail):
        if len(tail) is not 2:
            raise ValueError
        if tail is None or not isinstance(tail[0], int) or not isinstance(tail[1], int):
            raise TypeError
        self.gameWindow.addch(int(tail[0]), int(tail[1]), ' ')

    def destroyWindow(self):
        curses.endwin()

    def getScreenSizes(self) -> dict:
        return {"screenHeight": self.screenHeight, "screenWidth" : self.screenWidth}



