import random
score_comp = 0
score_User = 0
while True:
    User = input("Enter a choice (rock, paper, scissors): ")
    actions = ["rock", "paper", "scissors"]
    AI = random.choice(actions)
    print(f"\nYou chose {User}, computer chose {AI}.\n")

    if User == AI:
        print(f"Both players selected {User}. It's a tie!")
    elif User == "rock":
        if AI == "scissors":
            print("Rock smashes scissors! You win!")
            score_User = score_User + 1
        else:
            print("Paper covers rock! You lose.")
            score_comp = score_comp + 1
    elif User == "paper":
        if AI == "rock":
            print("Paper covers rock! You win!")
            score_User = score_User + 1
        else:
            print("Scissors cuts paper! You lose.")
            score_comp = score_comp + 1
    elif User == "scissors":
        if AI == "paper":
            print("Scissors cuts paper! You win!")
            score_User = score_User + 1
        else:
            print("Rock smashes scissors! You lose.")
            score_comp = score_comp + 1

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Your Score: ",score_User)
        print("Computer score: ",score_comp)
        break