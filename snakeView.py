import random
import curses

class SnakeView:
    
    def __init__(self):
        self.REFRESH_RATE = 100
        self.screen = curses.initscr()
        self.screenHeight, self.screenWidth = self.screen.getmaxyx()
        # No cursor in the screen
        curses.curs_set(0)

    def createWindow(self):
        self.gameWindow = curses.newwin(self.screenHeight, self.screenWidth, 0, 0)
        self.gameWindow.keypad(1)
        self.gameWindow.timeout(self.REFRESH_RATE)
        # Food screen centered
        return self.gameWindow
    
    def printSnake(self, snake):
        try:
            self.gameWindow.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
        except:
            print("The program couldn't print the snake")
            self.destroyWindow()
        
    def printFood(self, food):
        self.gameWindow.addch(food[0], food[1], curses.ACS_PI)

    def printSnakeTail(self, tail):
        self.gameWindow.addch(int(tail[0]), int(tail[1]), ' ')

    def destroyWindow(self):
        curses.endwin()
        quit()

    def getScreenSizes(self) -> dict:
        return {"screenHeight": self.screenHeight, "screenWidth" : self.screenWidth}



