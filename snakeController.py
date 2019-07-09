import curses

class SnakeController:
    
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.gameWindow = self.view.createWindow()
        self.view.printFood(self.model.getFood())

    def snakeInitDirection(self):
        self.snakeDirection = curses.KEY_RIGHT

    def snakeNextDirection(self):
        self.nextSnakeDirection = self.gameWindow.getch()
        self.snakeDirection = self.snakeDirection if self.nextSnakeDirection == -1 else self.nextSnakeDirection

    def snakeNewHead(self):
        newHead = [self.model.getSnakeCoordinates()[0][0], self.model.getSnakeCoordinates()[0][1]]
        # Snake control
        if self.snakeDirection == curses.KEY_DOWN:
            newHead[0] += 1
        if self.snakeDirection == curses.KEY_UP:
            newHead[0] -= 1
        if self.snakeDirection == curses.KEY_LEFT:
            newHead[1] -= 1
        if self.snakeDirection == curses.KEY_RIGHT:
            newHead[1] += 1
        self.model.insertSnakeHead(newHead)
    
    def snakeIsDied(self):
        screenSize = self.view.getScreenSizes()
        snakeCoordinates = self.model.getSnakeCoordinates()
        screenHeight = screenSize["screenHeight"]
        screenWidth = screenSize["screenWidth"]
        return True if snakeCoordinates in [0, screenHeight] or snakeCoordinates[0][1] in [0, screenWidth] or snakeCoordinates[0] in snakeCoordinates[1:] else False

    def snakeEatFood(self):
        if self.model.isSnakeEatingFood():
            newFood = self.model.getNewFoodCoordinates()
            self.view.printFood(newFood)
        else:
            tail = self.model.getSnakeCoordinates().pop()
            self.view.printSnakeTail(tail)

    def snakeRefresh(self):
        self.view.printSnake(self.model.getSnakeCoordinates())

    def closeGame(self):
        self.view.destroyWindow()