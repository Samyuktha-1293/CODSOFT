import random

def user_selection():
    while True:
        print("Choose one: 1: Rock, 2: Paper, 3: Scissors")
        user_choice = input().strip()
        if user_choice in ['1', '2', '3']:
            return user_choice
        else:
            print("Invalid choice. Please choose only 1, 2, or 3.")

def selected_choice(choice):
    if choice == '1':
        return 'rock'
    elif choice == '2':
        return 'paper'
    else:
        return 'scissor'

def system_choice():
    choices = ['rock', 'paper', 'scissor']
    return random.choice(choices)

def evaluate_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissor') or (user_choice == 'scissor' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You won"
    else:
        return "Computer wins!"

def play_again():
    return input("Do you want to play again? (yes/no): ").strip().lower() == 'yes'

print("Welcome to Rock, Paper, Scissor!")

while True:
    user_choice = user_selection()
    user_choice_name = selected_choice(user_choice)
    computer_choice = system_choice()

    print(f"You chose: {user_choice_name}")
    print(f"Computer chose: {computer_choice}")

    output = evaluate_winner(user_choice_name, computer_choice)
    print(output)

    if not play_again():
        break


