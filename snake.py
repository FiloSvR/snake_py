import random
import curses

REFRESH_RATE = 100

screen = curses.initscr()
# No cursor in the screen
curses.curs_set(0)
screenHeight, screenWidth = screen.getmaxyx()
gameWindow = curses.newwin(screenHeight, screenWidth, 0, 0)
gameWindow.keypad(1)
gameWindow.timeout(REFRESH_RATE)

# Snake initial position
snake_x = screenWidth/4
snake_y = screenHeight/2

snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2],
]

# Food screen centered
food = [screenHeight/2, screenWidth/2]
gameWindow.addch(food[0], food[1], curses.ACS_PI)

snakeDirection = curses.KEY_RIGHT

while True:
    nextSnakeDirection = gameWindow.getch()
    snakeDirection = snakeDirection if nextSnakeDirection == -1 else nextSnakeDirection

    if snake[0][0] in [0][screenHeight] or snake[0][1] in [0, screenWidth] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    newHead = [snake[0][0], snake[0][1]]
    # Snake control
    if snakeDirection == curses.KEY_DOWN:
        newHead[0] += 1
    if snakeDirection == curses.KEY_UP:
        newHead[0] -= 1
    if snakeDirection == curses.KEY_LEFT:
        newHead[1] -= 1
    if snakeDirection == curses.KEY_RIGHT:
        newHead[1] += 1
    
    snake.insert(0, newHead)

    # Snake run into the food
    if snake[0] == food:
        food = None
        while food is None:
            newFood = [
                random.randint(1, screenHeight-1),
                random.randint(1, screenWidth-1)
            ]
            food = newFood if newFood not in snake else None
        gameWindow.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        gameWindow.addch(tail[0], tail[1], ' ')

