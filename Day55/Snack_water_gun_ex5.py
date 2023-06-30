import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Snake/Water/Gun): ").strip().lower()
        if user_choice in ['snake', 'water', 'gun']:
            return user_choice
        else:
            print("Invalid choice! Please try again.")

def get_computer_choice():
    choices = ['snake', 'water', 'gun']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    choices_matrix = [
        [0, 1, 2],
        [2, 0, 1],
        [1, 2, 0]
    ]

    result_matrix = ['Draw', 'You win!', 'Computer wins!']
    player_index = {'snake': 0, 'water': 1, 'gun': 2}

    return result_matrix[choices_matrix[player_index[player_choice]][player_index[computer_choice]]]

def play_game():
    print("Welcome to Snake Water Gun!")
    print("You will be playing against the computer.")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("Thank you for playing Snake Water Gun!")

# Start the game
play_game()
