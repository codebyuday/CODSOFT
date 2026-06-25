import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'scissors' and computer == 'paper') or \
       (user == 'paper' and computer == 'rock'):
        return "win"
    return "lose"

def display_result(user, computer, result):
    print(f"\nYour choice:      {user.upper()}")
    print(f"Computer's choice: {computer.upper()}")
    print("-" * 30)
    if result == "tie":
        print("Result: It's a TIE!")
    elif result == "win":
        print("Result: You WIN!")
    else:
        print("Result: You LOSE!")

def display_score(user_score, computer_score, ties):
    print("\n--- SCOREBOARD ---")
    print(f"You: {user_score}  |  Computer: {computer_score}  |  Ties: {ties}")
    print("------------------")

def play_game():
    user_score = 0
    computer_score = 0
    ties = 0
    
    print("=" * 40)
    print("   ROCK - PAPER - SCISSORS")
    print("=" * 40)
    print("Rules:")
    print("  Rock beats Scissors")
    print("  Scissors beats Paper")
    print("  Paper beats Rock")
    print("=" * 40)
    
    while True:
        print("\nChoose: rock, paper, or scissors (or 'quit' to exit)")
        user_input = input("Your choice: ").strip().lower()
        
        if user_input == 'quit':
            break
        
        if user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        computer = get_computer_choice()
        result = determine_winner(user_input, computer)
        
        display_result(user_input, computer, result)
        
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        else:
            ties += 1
        
        display_score(user_score, computer_score, ties)
    
    print("\n" + "=" * 40)
    print("       FINAL RESULTS")
    print("=" * 40)
    display_score(user_score, computer_score, ties)
    print("\nThanks for playing!")

if __name__ == "__main__":
    play_game()
