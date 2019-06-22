import curses

class SnakeController:
    
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.gameWindow = self.view.createWindow()
        self.model.snakeInit()
        self.view.printFood(self.model.getFood())

    def snakeInitDirection(self):
        self.snakeDirection = curses.KEY_RIGHT

    def snakeNextDirection(self):
        self.nextSnakeDirection = self.gameWindow.getch()
        self.snakeDirection = self.snakeDirection if self.nextSnakeDirection == -1 else self.nextSnakeDirection

    def snakeNewHead(self):
        newHead = [self.model.getSnake()[0][0], self.model.getSnake()[0][1]]
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
        return True if self.model.getSnake() in [0, self.view.getScreenHigh()] or self.model.getSnake()[0][1] in [0, self.view.getScreenWidth()] or self.model.getSnake()[0] in self.model.getSnake()[1:] else False

    def snakeEatFood(self):
        if self.model.isSnakeEatingFood():
            newFood = self.model.getNewFood()
            self.view.printFood(newFood)
        else:
            tail = self.model.getSnake().pop()
            self.view.printSnakeTail(tail)

    def snakeRefresh(self):
        self.view.printSnake(self.model.getSnake())

    def closeGame(self):
        self.view.destroyWindow()