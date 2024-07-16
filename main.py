import random as r

# rock paper scisser
#1 i need user input to be read and compared
#2 I need the pc to pick a random choice of rock paper or scissors 
# then i need to compare them
game_on = True
while game_on == True:
    # players choice done, and input saved to a variable for use later
    print("Hello! Welcome to the awesome game of Rock Paper Scissors!")
    player_choice = input("Enter Your choice, 'rock', 'paper', 'scissors' or 'quit to stop playing \n\n").lower()
    if player_choice == 'quit':
        print("Goodbye, Thanks for playing with me!")
        game_on = False
        break

    # moving onto the AI's choice
    #We imported random as r and then give the r.choice a [list form of options]
    computer_choice = r.choice(["rock","paper","scissors"])
    print(computer_choice)

    if player_choice == "paper" and computer_choice == "rock":
        print(f"You have chosen: {player_choice}")
        print(f"The AI has chosen: {computer_choice}")
        
        print(f"\nThe player has won {player_choice} beats {computer_choice}\n")
        
    elif computer_choice == "paper" and player_choice == "rock":
        print(f"You have chosen: {player_choice}")
        print(f"The AI has chosen: {computer_choice}")
        
        print(f"\nThe AI has won {computer_choice} beats {player_choice}\n")
        
    elif player_choice == "rock" and computer_choice == "scissors":
        print(f"You have chosen: {player_choice}")
        print(f"The AI has chosen: {computer_choice}")
        
        print(f"\nThe player has won {player_choice} beats {computer_choice}\n")
        
    elif computer_choice == "rock" and player_choice == "scissors":
        print(f"You have chosen: {player_choice}")
        print(f"The AI has chosen: {computer_choice}")
        
        print(f"\nThe AI has won {computer_choice} beats {player_choice}\n")
        
    elif player_choice == "scissors" and computer_choice == "paper":
        print(f"You have chosen: {player_choice}")
        print(f"The AI has chosen: {computer_choice}")
        
        print(f"\nThe player has won {player_choice} beats {computer_choice}\n")
        
    elif computer_choice == "scissors" and player_choice == "paper":
        print(f"You have chosen: {player_choice}")
        print(f"The AI has chosen: {computer_choice}")
        
        print(f"\nThe AI has won {computer_choice} beats {player_choice}\n")
        
        
    elif player_choice == computer_choice:
        print(f"You have chosen: {player_choice}")
        print(f"The AI has chosen: {computer_choice}")
        
        print(f"\nTIE GAME\n")
        
  
    else:
        f"Error try again."
        
        
        
        
    
