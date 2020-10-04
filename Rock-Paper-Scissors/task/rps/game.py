# Write your code here
import random

options_dict = {"1": "paper", "2": "scissors", "3": "rock"}
#rating = dict()
current_rating = 0

print('Enter your name:', end=" ")
user_name = input()
print('Hello,', user_name, sep=" ")

ratings_file = open('rating.txt', 'r')
for line in ratings_file:
    args = line.split(" ")
    if args[0] == user_name:
        current_rating = int(args[1])

while True:
    user_move = input()
    computer_move = options_dict[str(random.randint(1, 3))]

    if user_move not in ("rock", "scissors", "paper", "!exit", "!rating"):
        print("Invalid input")
    elif user_move == "!exit":
        print("Bye!")
        break
    elif user_move == "!rating":
        print('Your rating:', current_rating, sep=' ')
    elif user_move == computer_move:
        print("There is a draw (" + user_move + ")")
        current_rating += 50
    elif user_move == "paper":
        if computer_move == "rock":
            print("Well done. The computer chose " + computer_move + " and failed")
            current_rating += 100
        else:
            print("Sorry, but the computer chose " + computer_move)
    elif user_move == "scissors":
        if computer_move == "paper":
            print("Well done. The computer chose " + computer_move + " and failed")
            current_rating += 100
        else:
            print("Sorry, but the computer chose " + computer_move)
    elif user_move == "rock":
        if computer_move == "scissors":
            print("Well done. The computer chose " + computer_move + " and failed")
            current_rating += 100
        else:
            print("Sorry, but the computer chose " + computer_move)