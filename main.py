import time
from turtle import Screen
from snake import Snake
from Food import Food
from skateboard import Skateboard
from outline import Outline

my_screen = Screen()
my_screen.tracer(0)
my_screen.setup(width=600, height=600)
my_screen.title("The Snake Game")
my_screen.bgcolor("black")

skateboard = Skateboard()
outline = Outline()
snake = Snake()
food = Food()


def snake_game():
    my_screen.listen()
    my_screen.onkey(snake.up, "Up")
    my_screen.onkey(snake.down, "Down")
    my_screen.onkey(snake.right, "Right")
    my_screen.onkey(snake.left, "Left")

    is_game_on = True
    while is_game_on:
        my_screen.update()
        time.sleep(0.1)

        snake.move()
        # Detect Food And Increase Score
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            skateboard.score_increase()
            #     Detect Game Over
        if snake.head.xcor() > 252 or snake.head.xcor() < -245 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
            skateboard.high_Score()
            is_game_on = False

            # Detect collision with tail
        for segment in snake.segments[2:]:

            if snake.head.distance(segment) < 15:
                is_game_on = False
                skateboard.high_Score()


ask_game = True
while ask_game:
    user_choice = my_screen.textinput("Snake Game",  "Do wanna play Y for yes and N for No").lower()
    if user_choice == "y":
        snake_game()
        snake.reset()

    else:
        ask_game = False


my_screen.exitonclick()
