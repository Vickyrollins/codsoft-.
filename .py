import random
def play_game():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to make a choice. Type 'quit' to exit the game.\n")

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.\n")
            continue
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!\n")
            user_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1
        print(f"Score: You {user_score} - {computer_score} Computer\n")
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            break

# Run the game
play_game()
