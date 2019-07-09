from snakeView import SnakeView
from snakeModel import SnakeModel
from snakeController import SnakeController

view = SnakeView()
model = SnakeModel(view.getScreenSizes())
controller = SnakeController(view, model)

controller.snakeInitDirection()

while True:
    controller.snakeNextDirection()
    if controller.snakeIsDied():
        controller.closeGame()
    controller.snakeNewHead()
    controller.snakeEatFood()
    controller.snakeRefresh()

