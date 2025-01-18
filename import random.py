import random
def play_game():
    userscore = 0
    computerscore = 0
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to make a choice. Type 'quit' to exit the game.\n")
    while True:
        userchoice = input("Choose rock, paper, or scissors: ").lower()
        if userchoice == "quit":
            print("Thank you for playing!")
            break
        if userchoice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.\n")
            continue
        computerchoice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computerchoice}")
        if userchoice == computerchoice:
            print("It's a tie!\n")
        elif (userchoice == "rock" and computerchoice == "scissors") or \
             (userchoice == "scissors" and computerchoice == "paper") or \
             (userchoice == "paper" and computerchoice == "rock"):
            print("You win this round!\n")
            userscore += 1
        else:
            print("Computer wins this round!\n")
            computerscore += 1
        print(f"Score: You {userscore} - {computerscore} Computer\n")
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            print(f"Final Score: You {userscore} - {computerscore} Computer")
            break
play_game()