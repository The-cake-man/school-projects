import random
user_input = input("players(1, 2):")
if user_input =="1":
    player1_action = input("choose (rock, paper, scissors):")
else: player1_action = input("player 1 choose(rock, paper, scissors):")
possible_actions = ["rock", "paper", "scissors"]
if user_input == "1":
    player2_action = random.choice(possible_actions)
if user_input == "2":
    player2_action = input("player 2 choose(rock, paper, scissors):")
if player1_action == player2_action:
    print(f"both players selected {player1_action}. It's a tie!")
if(player1_action) == "rock":
    if(player2_action) == "scissors":
        if(user_input) == "1":
            print("rock smashes scissors! You win!")
        if(user_input) == "2":
            print("rock smashes scissors! Player 1 wins!")
    if(player2_action) == "paper":
        if(user_input) == "1":
            print("paper covers rock! You lose.")
        if(user_input) == "2":
            print("paper covers rock! Player 2 wins.")
if(player1_action) == "paper":
    if(player2_action) == "rock":
        print("paper covers rock! Player 1 wins!")
    if(player2_action) =="scissors":
        print("scissors cuts paper! Player 2 wins.")
if(player1_action) == "scissors":
    if(player2_action) == "paper":
        if user_input == "1":
            print("scissors cuts paper! You win!")
        if user_input == "2":
            print("scissors cuts paper! Player 1 wins!")
    if(player2_action) == "rock":
        if user_input == "1":
            print("rock smashed scissors! You lose.")
        if user_input == "2": print("rock smashed scissors! Player 2 wins.")