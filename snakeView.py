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
        snake_y = snake[0][0]
        snake_x = snake[0][1]
        if not isinstance(snake_x, int) or not isinstance(snake_y, int):
            raise TypeError
        if snake_y > self.screenHeight or snake_x > self.screenWidth:
            raise ValueError
        try:
            self.gameWindow.addch(snake_y, snake_x, curses.ACS_CKBOARD)
        except Exception:
            raise curses.error
        
    def printFood(self, food):
        try:
            self.gameWindow.addch(food[0], food[1], curses.ACS_PI)
        except Exception:
            raise curses.error

    def printSnakeTail(self, tail):
        if len(tail) is not 2:
            raise ValueError
        if tail is None or not isinstance(tail[0], int) or not isinstance(tail[1], int):
            raise TypeError
        try:
            self.gameWindow.addch(int(tail[0]), int(tail[1]), ' ')
        except Exception:
            raise curses.error    

    def destroyWindow(self):
        curses.endwin()

    def getScreenSizes(self) -> dict:
        return {"screenHeight": self.screenHeight, "screenWidth" : self.screenWidth}



