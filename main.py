import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(player.move, "Up")

scoreboard = Scoreboard()

cars_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars_manager.move(scoreboard.level)
    game_is_on = player.collision_with_car(cars_manager.cars)
    if player.ycor() >= FINISH_LINE_Y:
        player.new_level()
        scoreboard.add_level()
        cars_manager.add_car()

scoreboard.game_over()
