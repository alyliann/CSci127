#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: November 9, 2021
#This program creates a game of rock paper scissors between the user and a computer

import random

winner = ""
playerMove = int(input("enter 1 for rock, 2 for paper, or 3 for scissors: "))

while playerMove > 0:
    computerMove = random.randrange(1,4)
    print("computerMove: ", computerMove)
    if playerMove > 3:
        winner = "invalid"
    elif playerMove > 0:
        if playerMove == computerMove:
            winner = "draw"
        elif playerMove == 1 and computerMove == 3:
            winner = "human"
        elif playerMove == 3 and computerMove == 1:
            winner = "computer"
        elif playerMove > computerMove:
            winner = "human"
        elif playerMove < computerMove:
            winner = "computer"
    print("round finished and winner is: ", winner)
    playerMove = int(input("enter 1 for rock, 2 for paper, or 3 for scissors: "))
if playerMove < 1:
    print("round finished and winner is: ", winner)

