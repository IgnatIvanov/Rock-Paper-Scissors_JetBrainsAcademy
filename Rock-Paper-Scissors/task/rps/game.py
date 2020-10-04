# Write your code here
import random

options_dict = list(['scissors', 'paper', 'rock'])
all_options = list(['rock', 'fire', 'scissors', 'snake', 'human',
                    'tree', 'wolf', 'sponge', 'paper', 'air',
                    'water', 'dragon', 'devil', 'lightning', 'gun',
                    'rock', 'fire', 'scissors', 'snake', 'human',
                    'tree', 'wolf', 'sponge', 'paper', 'air',
                    'water', 'dragon', 'devil', 'lightning', 'gun'])
current_rating = 0

print('Enter your name:', end=" ")
user_name = input()
print('Hello,', user_name, sep=" ")

ratings_file = open('rating.txt', 'r')
for line in ratings_file:
    args = line.split(" ")
    if args[0] == user_name:
        current_rating = int(args[1])

dict_input = input()
if dict_input != '':
    options_dict = dict_input.split(',')
print("Okay, let's start")

while True:
    user_move = input()
    computer_move = options_dict[random.randint(0, len(options_dict)-1)]

    if user_move == "!exit":
        print("Bye!")
        break
    elif user_move == "!rating":
        print('Your rating:', current_rating, sep=' ')
    elif user_move == computer_move:
        print("There is a draw (" + user_move + ")")
        current_rating += 50
    elif user_move in options_dict:
        user_index = all_options.index(user_move)
        if computer_move in all_options[user_index:user_index+8]:
            print("Well done. The computer chose " + computer_move + " and failed")
            current_rating += 100
        else:
            print("Sorry, but the computer chose " + computer_move)
    else:
        print("Invalid input")
