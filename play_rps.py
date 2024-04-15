import random


def play_again_or_not():
    user_answer = input("Would you like to play again? (y/n): ")
    if user_answer.lower() == 'y':
        play_rps()
    else:
        print("Thank you for playing!")


def play_rps():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    player_choice = input("Enter your choice: ")
    print(f"Computer: {computer_choice}, Player: {player_choice}")
    if computer_choice == 'rock':
        if player_choice == 'scissors':
            print("You lose!")
        if player_choice == 'paper':
            print("You win!")
        if player_choice == 'rock':
            print("It is a tie!")
    if computer_choice == 'paper':
        if player_choice == 'scissors':
            print("You win!")
        if player_choice == 'paper':
            print("It is a tie!")
        if player_choice == 'rock':
            print("You lose!")
    if computer_choice == 'scissors':
        if player_choice == 'rock':
            print("You win!")
        if player_choice == 'paper':
            print("You lose!")
        if player_choice == 'scissors':
            print("It is a tie!")
    play_again_or_not()

