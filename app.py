#using import for template running game 
import random

def play_game():
    valid_choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice not in valid_choices:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(valid_choices)
        print(f"Computer chose {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You won!")
            player_score += 1
        else:
            print("You lost!")
            computer_score += 1

        print(f"Score: Player {player_score}, Computer {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()