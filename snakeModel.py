import random

class SnakeModel():

    SNAKE_SCREEN_HEIGHT_POSITIONING = 2
    SNAKE_SCREEN_WIDTH_POSITIONING = 4
    FOOD_SCREEN_POSITIONING = 2

    def __init__(self, screenSize):
        if  screenSize is None or not isinstance(screenSize['screenHeight'], int) or not isinstance(screenSize['screenWidth'], int):
            raise TypeError
        if screenSize["screenHeight"] < self.SNAKE_SCREEN_HEIGHT_POSITIONING or screenSize["screenWidth"] < self.SNAKE_SCREEN_WIDTH_POSITIONING:
            raise ValueError
        self.screenHeight = screenSize["screenHeight"]
        self.screenWidth = screenSize["screenWidth"]
        self.foodCoordinates = [
            self.screenHeight//self.FOOD_SCREEN_POSITIONING, 
            self.screenWidth//self.FOOD_SCREEN_POSITIONING
            ]
        snake_x = self.screenWidth//self.SNAKE_SCREEN_WIDTH_POSITIONING
        snake_y = self.screenHeight//self.SNAKE_SCREEN_HEIGHT_POSITIONING
        self.snakeCoordinates = [
            [snake_y, snake_x],
            [snake_y, snake_x-1],
            [snake_y, snake_x-2],
        ]

    def insertSnakeHead(self, head: list):
        if len(head) is not 2:
            raise ValueError
        if head is None or not isinstance(head[0], int) or not isinstance(head[1], int):
            raise TypeError
        self.snakeCoordinates.insert(0, head)
    
    def isSnakeEatingFood(self):
        return True if self.snakeCoordinates[0] == self.foodCoordinates else False
    
    def getFoodCoordinates(self):
        return self.foodCoordinates
    
    def getSnakeCoordinates(self) -> list:
        return self.snakeCoordinates

    def getNewFoodCoordinates(self) -> list:
        food = None
        while food is None:
            newFoodCoordinates = [
                        random.randint(1, self.screenHeight-1),
                        random.randint(1, self.screenWidth-1)
                    ]
            food = newFoodCoordinates if newFoodCoordinates not in self.snakeCoordinates else None
        self.foodCoordinates = newFoodCoordinates
        return newFoodCoordinates
