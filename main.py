import random

while True:
    vals = ['rock', 'paper', 'scissors']
    player = None

    CPU = random.choice(vals)

    while player not in vals:
        player = input("Rock, paper or scissors?: ").lower()

    if player == CPU:
        print("Player: " + player)
        print("CPU: " + CPU)
        print("Tie!")

    elif player == "rock":
        if CPU == "paper":
            print("Player: " + player)
            print("CPU: " + CPU)
            print("You Lose!")
        if CPU == "scissors":
            print("Player: " + player)
            print("CPU: " + CPU)
            print("You Win!")

    elif player == "paper":
        if CPU == "scissors":
            print("Player: " + player)
            print("CPU: " + CPU)
            print("You Lose!")
        if CPU == "rock":
            print("Player: " + player)
            print("CPU: " + CPU)
            print("You Win!")

    elif player == "scissors":
        if CPU == "rock":
            print("Player: " + player)
            print("CPU: " + CPU)
            print("You Lose!")
        if CPU == "paper":
            print("Player: " + player)
            print("CPU: " + CPU)
            print("You Win!")

    answer = ['yes', 'no']
    play_Again = None
    while play_Again not in answer:
        play_Again = input("Play again? (yes/no): ").lower()

    if play_Again == "no":
            break
    elif play_Again == "yes":
            continue

print("Thanks for playing! Bye-Bye!")