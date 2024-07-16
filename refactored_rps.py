## refactored version
import random as r

game_on = True
## this method allows you to create a dictionary and use that instead of comparing each outcome.
def determine_winner(player,computer):
    winning_combos = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if player == computer:
        return "TIE GAME!"
    elif winning_combos[player] == computer:
        return "The Player has won!"
    else:
        return "The AI has won!"

while game_on:
    print("Hello! Welcome to the awesome game of Rock Paper Scissors!")
    player_choice = input("Enter your choice ('rock', 'paper', 'scissors') or 'quit' to stop playing: ").lower()
    if player_choice == 'quit':
        print("Goodbye, Thanks for playing with me!")
        game_on = False
        break
    
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        continue

    computer_choice = r.choice(["rock", "paper", "scissors"])
    print(f"You have chosen: {player_choice}")
    print(f"The AI has chosen: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(f"\n{result}\n")