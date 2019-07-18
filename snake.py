from snakeArcadeView import SnakeArcadeView
from snakeModel import SnakeModel
from snakeController import SnakeController

view = SnakeArcadeView()
model = SnakeModel(view.getScreenSizes())
controller = SnakeController(view, model)

controller.snakeInitDirection()

while True:
    controller.snakeNextDirection()
    controller.snakeNewHead()
    if controller.snakeIsDied():
        controller.closeGame("you died!")
    controller.snakeEatFood()
    controller. ()

