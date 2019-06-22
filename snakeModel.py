import random
class SnakeModel():

    def __init__(self, screenHight, screenWidth):
        self.screenHight = screenHight
        self.screenWidth = screenWidth
        self.food = [self.screenHight//2, self.screenWidth//2]
        
    def snakeInit(self):
        # Snake initial position
        snake_x = self.screenWidth//4
        snake_y = self.screenHight//2
        self.snake = [
            [snake_y, snake_x],
            [snake_y, snake_x-1],
            [snake_y, snake_x-2],
        ]

    def insertSnakeHead(self, head):
        self.snake.insert(0, head)
    
    def isSnakeEatingFood(self):
        return True if self.snake[0] == self.food else False
    
    def getFood(self):
        return self.food

    def setFood(self, newFood):
        self.food = newFood
    
    def getSnake(self):
        return self.snake

    def getNewFood(self):
        food = None
        while food is None:
            newFood = [
                        random.randint(1, self.screenHight-1),
                        random.randint(1, self.screenWidth-1)
                    ]
            food = newFood if newFood not in self.snake else None
        return newFood

