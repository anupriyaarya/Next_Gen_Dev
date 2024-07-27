import random

def game():
    while True:
        user = input("Enter a choice (rock, paper, scissors): ")
        user = user.lower()

        while user not in ["rock", "paper", "scissors"]:
            user = input("Invalid input. Please enter rock, paper or scissors: ")
            user = user.lower()

        possible_choices = ["rock", "paper", "scissors"]
        computer = random.choice(possible_choices)
        print(f"\nYou chose {user}, computer chose {computer}.\n")

        if user == computer:
            print(f"Both players selected {user}. It's a tie!")
        elif user == "rock":
            if computer == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user == "scissors":
            if computer == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    game()
