#Rock Paper Scissors vs.Python

option = ["Rock", "Paper", "Scissors"]
import random
player_1_wins = 0
player_2_wins = 0
while True:
    player_1 = input("Choose your weapon! ")
    player_2 = random.choice(option)
    print(f"And here is my counter! {player_2}")
    if player_1 == player_2:
        print("Tie!")
    elif player_1 == "Paper": 
        if player_2 == "Rock": 
            print("Player 1 Wins!")
            player_1_wins += 1
        else:
            print("Player 2 Wins!")
            player_2_wins += 1
    elif player_1 == "Rock": 
        if player_2 == "Scissors": 
            print("Player 1 Wins!")
            player_1_wins += 1
        else:
            print("Player 2 Wins!")
            player_2_wins += 1
    elif player_1 == "Scissors": 
        if player_2 == "Paper": 
            print("Player 1 Wins!")
            player_1_wins += 1
        else:
            print("Player 2 Wins!")
            player_2_wins += 1
    else:
        print("Oh no, try writing Paper, Scissors or Rock. Other options don’t work here!")

    print(f"Player 1: {player_1_wins} | Player 2: {player_2_wins}")

    if player_1_wins == 5:
        print("Player 1 wins!")
        print("Thank youu for playing <3")
    elif player_2_wins == 5:
        print("Player 2 Wins!")
        print("Thank youu for playing <3")
        break
