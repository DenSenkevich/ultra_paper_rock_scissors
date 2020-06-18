import random
import math

user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

default_options = ["paper", "rock", "scissors"]
plan = "A"
options = input().split(",")
if options == ['']:
    options = default_options
    plan = "B"
print("Okay, let's start")

rating = open("rating.txt", "r")
if any(line.startswith(user_name) for line in rating):
    for line in rating:
        if line.startswith(user_name):
            name, score = line.strip().split()
else:
    score = 0

while True:
    user_choice = input()
    comp_choice = random.choice(options)

    if user_choice == "!exit":
        print("Bye!")
        break
    if user_choice == "!rating":
        print(f"Your rating: {score}")
    if user_choice in options:
        if plan == "B":
            if user_choice == comp_choice:
                print(f"There is a draw {user_choice}")
                score = int(score) + 50
            elif user_choice == "paper" and comp_choice == "rock":
                print(f"Well done. Computer chose {comp_choice} and failed")
                score = int(score) + 100
            elif user_choice == "rock" and comp_choice == "scissors":
                print(f"Well done. Computer chose {comp_choice} and failed")
                score = int(score) + 100
            elif user_choice == "scissors" and comp_choice == "paper":
                print(f"Well done. Computer chose {comp_choice} and failed")
                score = int(score) + 100
            else:
                print(f"Sorry, but computer chose {comp_choice}")
        elif plan == "A":
            score_list = options[(options.index(user_choice) + 1):] + options[:options.index(user_choice)]
            if user_choice == comp_choice:
                print(f"There is a draw {user_choice}")
                score = int(score) + 50
            elif comp_choice in score_list[math.ceil(len(score_list) / 2):]:
                print(f"Well done. Computer chose {comp_choice} and failed")
                score = int(score) + 100
            else:
                print(f"Sorry, but computer chose {comp_choice}")
    else:
        print("Invalid input")

