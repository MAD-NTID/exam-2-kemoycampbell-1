"""
@author: <Your name>
date: <today's date>
Project code name: HandBattle
Purpose:
    A program that play rock, paper, scissors
"""

import datetime
import random

#PREDEFINED
"""
    This function will print the header containing 
    Rock, paper,scissors as well as today's date and time
"""
def game_header():
    print("==============================")
    rock = "Rock:🗿"
    paper = "Paper:📃"
    scissors = "Scissors:✂️"
    print(f"{rock} {paper} {scissors}")
    print("\n\tGame Version 0.1")
    print("==============================\n")
    now = datetime.datetime.now()
    print("Date and Time:",now.strftime("%d/%m/%Y %H:%M:%S"))

#PREDEFINED
"""
    This function generate an xp.
    The function first generate an xp
    then multiply that by the round number

    Parameter:
        round: The current round in the game

    returns the xp for the round
"""
def generate_xp(round):
    min_xp = 1
    max_xp = 30
    xp = random.randint(min_xp, max_xp)
    return xp * round

#PREDEFINED
"""
    This function will randomly pick a choice for the computer.
    This will return one of the following, "rock", "paper" or "scissor"
"""
def get_computer_choice():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)


#STUDENT CODE HERE
#STUDENT FUNCTIONS HERE



#PREDEFINED
def main():
    #STUDENT CODE HERE - VARIABLES DECLARATION
    while True:
        #STUDENT CODE HERE
        pass #Remove this before coding


#PREDEFINED
main()
