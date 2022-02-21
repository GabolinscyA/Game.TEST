import random
player_1 = 100
player_2 = 100
player_3 = 100
AI_1 = 100

def turn_1():
    P_action_1 = input("Player 1 turn input screen.'end' to move onto next player")
    if P_action_1 == "end":
        turn_2()
def turn_2():
    P_action_2 = input("Player 2 turn input screen.'end' to move onto next player")
    if P_action_2 == "end":
        turn_3()
def turn_3():
    P_action_3 = input("Player 3 turn input screen.'end' to move onto next player")
    if P_action_3 == "end":
        turn_AI_1()
def turn_AI_1():
    print("Enemy AI turn screen text. Returning to player 1 turn after AI action taken")
    turn_1()
turn_1()
