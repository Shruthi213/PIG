import _random
import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players(2-4) : ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print("Must be between 2-4")
            break
        else:
            print("Invalid enter 2-4")
    else:
        print("Invalid Input")
max_score = 50
player_score = [0 for i in range(players)]

while max(player_score) < max_score:

    for player_idx in range(players):
        current_score = 0
    while True:
        should_roll = input("would you like to roll: (y): ")
        if should_roll.lower() != "y":
            break

        value = roll()
        if value == 1:
            print("Your score is 1")
            break
        else:
            current_score += value
            print("Your rolled  :  ", value, "times")

        player_score[player_idx] += current_score
        print("Your score is :", player_score[player_idx])

