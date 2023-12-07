import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.new_car()
    car_manager.move()

    # collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            print("turtle touched car")
            scoreboard.game_over()
            game_is_on = False

    # crossed finish line
    if player.finish_line():
        player.starting_line()
        car_manager.increase_speed()
        scoreboard.scored()

screen.exitonclick()

