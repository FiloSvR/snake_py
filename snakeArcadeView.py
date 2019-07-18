import random
import arcade
import os

# Set up the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snake"

class Snake():
    def __init__(self, x, y, width, height, angle, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.image = image

class DrawSnake(Snake):
    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, self.width, self.heigh, self.image, self.angle)
    

class SnakeArcadeView(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    
    
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
            arcade.draw_text("draw_bitmap", 483, 3, arcade.color.BLACK, 12)
            snake_head = arcade.load_texture("images/snake_head.png")
            scale = .1
            arcade.draw_texture_rectangle(snake_y, snake_x, scale * snake_head.width, scale * snake_head.height, snake_head, 90)
            arcade.finish_render()
        except Exception:
            raise ValueError #TODO chanege error type
    
    def printFood(self, food):
        arcade.draw_text("draw_bitmap", 483, 3, arcade.color.BLACK, 12)
        apple = arcade.load_texture("images/apple.png")
        scale = .1
        arcade.draw_texture_rectangle(food[0], food[1], scale * apple.width, scale * apple.height, apple, 0)
        arcade.finish_render()

    def printSnaketail(self, tail):
        pass

    def destroyWindow(self):
        pass

    def getScreenSizes(self) -> dict:
        return {"screenHeight": self.screenHeight, "screenWidth" : self.screenWidth}

    def render():
        arcade.run()
