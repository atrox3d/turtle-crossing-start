import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.moveup, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    scoreboard.update_score()

    carmanager.create_car()
    carmanager.move_cars()
    #
    #   detect car collision
    #
    for car in carmanager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()
    #
    #   detect succesful crossing
    #
    if player.is_at_finishline():
        player.goto_start()
        carmanager.levelup()
        scoreboard.levelup()
screen.exitonclick()
