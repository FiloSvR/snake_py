import random

class SnakeModel():

    SNAKE_SCREEN_HEIGHT_POSITIONING = 2
    SNAKE_SCREEN_WIDTH_POSITIONING = 4
    FOOD_SCREEN_POSITIONING = 2

    def __init__(self, screenHeight: int, screenWidth: int):
        # TODO How do I clean this IF ??
        if  not isinstance(screenHeight, int) or not isinstance(screenWidth, int):
            raise TypeError
        if screenHeight < self.SNAKE_SCREEN_HEIGHT_POSITIONING or screenWidth < self.SNAKE_SCREEN_WIDTH_POSITIONING:
            raise ValueError

        self.screenHeight = screenHeight
        self.screenWidth = screenWidth
        self.snakeInit()
        self.foodInit()
        
    def snakeInit(self):
        snake_x = self.screenWidth//self.SNAKE_SCREEN_WIDTH_POSITIONING
        snake_y = self.screenHeight//self.SNAKE_SCREEN_HEIGHT_POSITIONING
        self.snakeCoordinates = [
            [snake_y, snake_x],
            [snake_y, snake_x-1],
            [snake_y, snake_x-2],
        ]

    def foodInit(self):
        self.foodCoordinates = [self.screenHeight//self.FOOD_SCREEN_POSITIONING, self.screenWidth//self.FOOD_SCREEN_POSITIONING]

    def insertSnakeHead(self, head: list):
        if head is None:
            raise TypeError
        if len(head) is not 2:
            raise ValueError
        self.snakeCoordinates.insert(0, head)
    
    def isSnakeEatingFood(self):
        return True if self.snakeCoordinates[0] == self.foodCoordinates else False
    
    def getFood(self):
        return self.foodCoordinates
    
    def getSnake(self):
        return self.snakeCoordinates

    def getNewFoodCoordinates(self):
        food = None
        while food is None:
            newFoodCoordinates = [
                        random.randint(1, self.screenHeight-1),
                        random.randint(1, self.screenWidth-1)
                    ]
            food = newFoodCoordinates if newFoodCoordinates not in self.snakeCoordinates else None
        self.foodCoordinates = newFoodCoordinates
        return newFoodCoordinates

    def setFoodCoordinates(self, newFood):
        self.foodCoordinates = newFood
