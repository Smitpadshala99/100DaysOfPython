import random

def result(pc,cc):
    choices_matrix = [
        [0,1,2],
        [2,0,1],
        [1,2,0]
    ]
    rmatrix = ['Draw', 'You Win!', 'Computer Win!']
    pindex = {'snake':0, 'water':1, 'gun':2}
    return rmatrix[choices_matrix[pindex[pc]][pindex[cc]]]

print("Welcomeu to Snake Water Gun!")
while True:
    User_choice = input("Enter your choice (Snake/Water/Gun): ").strip().lower()
    if User_choice in ['snake', 'water', 'gun']:
        User_choice = User_choice
    else:
        print("Invalid choice")

    choices = ['snake', 'water', 'gun']
    computer_choice = random.choice(choices)

    print("Your choice: ", User_choice)
    print("Computer's choice: ", computer_choice)

    winner = result(User_choice,computer_choice)
    print(winner)

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        break
    